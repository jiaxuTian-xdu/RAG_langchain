import os
from pathlib import Path
from typing import List,Dict,Optional
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
# --- 从原文件导入必要的类和函数 ---
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from fastapi import FastAPI, File, UploadFile, HTTPException, Form  
from pydantic import BaseModel
from rank_bm25 import BM25Okapi
import json
from qa_system import QASystem
from utils import chunk_md_content,load_existing_data,save_all_data ,message_change,ensure_department_exists,pdf_to_markdown,save_all_department_vector_stores,load_all_department_vector_stores
from shouce import (
    load_index_and_map, 
    find_markdown_file,
)
from fastapi.middleware.cors import CORSMiddleware

from config import  EMBEDDING_MODEL_NAME,SHOUCE_INDEX_PATH,ID_MAP_PATH,MARKDOWN_ROOT_FOLDER,SPLITS_FILE,INDEX_PATH
from config import DEPARTMENTS_DIR,vector_stores

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}
from common.mysql import initialize_database,insert_department_doc,insert_file_master
from chunks_minji import hybrid_search
with open('common/prompts.json', 'r', encoding='utf-8') as f:
    PROMPT_CONFIG = json.load(f)
# --- 配置常量 (与原文件保持一致) ---

global vector_store, all_splits, bm25_instance
vector_store = None               
all_splits = []
bm25_instance = None
# --- 全局变量初始化 ---
embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL_NAME,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

# --- FastAPI 应用初始化 ---
app = FastAPI(
    title="RAG知识库API",
    description="提供文档上传、知识库查询功能。"
)

# --- 启动事件：加载现有数据,初始化数据库 ---
app.mount(
    "/word2md",
    StaticFiles(directory=MARKDOWN_ROOT_FOLDER),
    name="manual_assets"
)

@app.on_event("startup")
def on_startup():
    global vector_store, all_splits, bm25_instance
    vector_store , all_splits , bm25_instance = load_existing_data()
    print("正在加载部门向量库...")  
    DEPARTMENTS_DIR.mkdir(parents=True, exist_ok=True)

    vector_stores.update(load_all_department_vector_stores(embedding_model))
    print("部门向量库加载完成。")
    initialize_database()


# --- 关闭事件：保存所有数据 ---
@app.on_event("shutdown")
def on_shutdown():
    save_all_data()

# --- API 模型定义 ---

class QueryRequest(BaseModel):
    query: str
    k: int = 3
    context_range: int = 0

class QueryResponse(BaseModel):
    summary:str
    query: str
    results: List[dict]

class ManualResponse(BaseModel):
    query: str
    manual_content: Optional[str]
    filename: str
    scope_text: str
    images: List[str] = Field(default_factory=list)
    error: Optional[str] = None

class DocumentAddResponse(BaseModel):
    message: str
    filename: Optional[str] = None
    status: Optional[str] = "success"
    chunks_added: Optional[int] = None
    department: Optional[str] = None
    dept_doc_id: Optional[int] = None
    file_master_id: Optional[int] = None
# --- API 路由定义 ---
vector_stores: dict[str, FAISS] = {}


@app.post("/add_documents/" , response_model=List[DocumentAddResponse])
async def add_documents_to_knowledge_base( 
    file: List[UploadFile] = File(...),
    department: str = Form(...)
 ):
    results: List[DocumentAddResponse] = []
    if not department:
        return [DocumentAddResponse(message="文件类型参数不能为空", status="error")]
 
    try:
        # 这个函数现在会创建存放MD文件的目录，并尝试加载（但不创建）向量库目录
        ensure_department_exists(department)
    except Exception as e:
        return [DocumentAddResponse(message=f"类型 '{department}' 初始化失败: {str(e)}", status="error")]
 
    # *** 关键修改：在上传文件循环之前，确保向量库的保存目录存在 ***
    # 这能保证即使是新部门，后续的save_local也不会因目录不存在而失败
    try:
        department_vector_store_path = DEPARTMENTS_DIR / department
        department_vector_store_path.mkdir(parents=True, exist_ok=True)
        # 如果是新部门，此时vector_stores[department]还不存在，但目录已经准备好了
        if department not in vector_stores:
            print(f"为新部门 '{department}' 准备了向量库存储目录: {department_vector_store_path}")
    except Exception as e:
        return [DocumentAddResponse(message=f"无法为部门 '{department}' 创建存储目录: {str(e)}", status="error")]
 
    for f in file:
        md_path = None
        try:
            # ... (文件处理逻辑保持不变) ...
            file_type = Path(f.filename).suffix.lower()
            if file_type == ".pdf":
                md_save_dir = DEPARTMENTS_DIR / department
                md_path = await pdf_to_markdown(f, save_path=md_save_dir)
            elif file_type == ".md":
                safe_filename = Path(f.filename).name
                md_path = DEPARTMENTS_DIR / department / safe_filename
                content = await f.read()
                with open(md_path, "wb") as f_write:
                    f_write.write(content)
            else:
                raise ValueError("仅支持 PDF (.pdf) 和 Markdown (.md) 文件")
 
            with open(md_path, "r", encoding="utf-8") as f_read:
                splits = chunk_md_content(f_read.read(), f.filename)
 
            # *** 关键修改点 ***
            # 当为新部门首次添加文档时，确保目录已经存在，然后再创建向量库
            if department not in vector_stores:
                print(f"为新部门 '{department}' 在内存中创建向量库...")
                # 此时目录已在上方循环开始前创建，此处创建向量库是安全的
                vector_stores[department] = FAISS.from_documents(splits, embedding_model)
            else:
                print(f"向已存在的部门 '{department}' 的向量库添加文档...")
                vector_stores[department].add_documents(splits)
 
            dept_doc_id = insert_department_doc(f.filename, department)
            file_master_id = insert_file_master(f.filename, file_type, department)
 
            results.append(DocumentAddResponse(
                message=f"文件 '{f.filename}' 已成功添加到类型 '{department}'。",
                filename=f.filename,
                chunks_added=len(splits),
                department=department,
                dept_doc_id=dept_doc_id,
                file_master_id=file_master_id
            ))
        except Exception as e:
            results.append(DocumentAddResponse(
                message=f"文件 '{f.filename}' 处理失败: {str(e)}",
                filename=f.filename,
                status="error"
            ))
 
    try:
        save_all_department_vector_stores(vector_stores)
    except Exception as e:
        print(f"警告：向量库持久化失败: {e}")
    return results


@app.post("/query/", response_model=QueryResponse, summary="查询知识库 (混合检索)")
async def query_knowledge_base_form( 
    query: str = Form(..., description="输入你的查询问题"),
    k: int = Form(3, description="返回最相关的片段数量"),
    context_range: int = Form(0, description="每个片段的上下文范围（前后各几个片段）")
 ):
    """
    通过表单界面查询知识库，使用混合检索（语义检索 + BM25）。
    - query: 查询问题
    - k: 返回最相关的片段数量
    - context_range: 返回每个相关片段的上下文范围（前后各几个片段）
    """
    global vector_store, all_splits, bm25_instance

    if not vector_store or not bm25_instance or not all_splits:
        raise HTTPException(status_code=503, detail="知识库未就绪，请检查服务器日志或稍后再试。")
 
    try:
        # 实例化QASystem并调用process_query获取AI答案
        qa_system = QASystem(vector_store, bm25_instance, all_splits)
        
        # 调用混合检索函数获取原始文档片段
        results_data = hybrid_search(
            vector_store=vector_store,
            bm25=bm25_instance,
            all_splits=all_splits,
            query=query,
            k=k,
            context_range=context_range
        )
        messages = message_change(results_data,query)
        ai_answer = qa_system.call_deepseek_api(messages)
        print(ai_answer)


        return QueryResponse(summary=ai_answer, query=query, results=results_data)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询过程中发生错误: {str(e)}")

@app.post("/query_by_department/", response_model=QueryResponse, summary="按部门查询知识库")
async def query_knowledge_base_by_department(
    query: str = Form(..., description="输入你的查询问题"),
    k: int = Form(3, description="返回最相关的片段数量"),
    context_range: int = Form(0, description="每个片段的上下文范围（前后各几个片段）"),
    department: str = Form(..., description="查询的部门")
):
    """
    通过表单界面按部门查询知识库，使用混合检索（语义检索 + BM25）。
    - query: 查询问题
    - k: 返回最相关的片段数量
    - context_range: 返回每个相关片段的上下文范围（前后各几个片段）
    - department: 查询的目标部门
    """
    # 检查指定部门的向量库是否存在
    if department not in vector_stores:
        raise HTTPException(status_code=404, detail=f"未找到部门 '{department}' 的知识库，请先上传文档。")
    
    # 获取该部门的向量库
    department_vector_store = vector_stores[department]

    try:
        # 实例化QASystem，传入部门向量库
        # 注意：BM25实例和all_splits在这里可能不是特定于部门的。
        # 如果它们也需要是部门特定的，你需要相应地修改数据结构和加载逻辑。
        # 假设当前混合检索可以复用全局的BM25和all_splits。
        qa_system = QASystem(department_vector_store, bm25_instance, all_splits)
        
        # 调用混合检索函数获取原始文档片段
        results_data = hybrid_search(
            vector_store=department_vector_store,
            bm25=bm25_instance,
            all_splits=all_splits,
            query=query,
            k=k,
            context_range=context_range
        )
        
        messages = message_change(results_data, query)
        ai_answer = qa_system.call_deepseek_api(messages)

        return QueryResponse(summary=ai_answer, query=query, results=results_data)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询部门 '{department}' 时发生错误: {str(e)}")
    
def collect_manual_images(md_file_path: str) -> List[str]:
    """Return sorted list of manual-related image paths."""
    manual_dir = os.path.dirname(md_file_path)
    images_dir = os.path.join(manual_dir, "images")
    if not os.path.isdir(images_dir):
        return []

    image_paths: List[str] = []
    for image_name in sorted(os.listdir(images_dir)):
        _, ext = os.path.splitext(image_name)
        if ext.lower() in IMAGE_EXTENSIONS:
            full_path = os.path.join(images_dir, image_name)
            rel_path = os.path.relpath(full_path, start=".")
            web_path = "/" + rel_path.replace("\\", "/").lstrip("./")
            image_paths.append(web_path)
    return image_paths

@app.post("/manual_query/", response_model=ManualResponse, summary="查询操作手册")
async def query_manual(
    query: str = Form(..., description="输入查询关键词")
):
    """
    根据用户查询从操作手册中检索相关内容：
    - query: 查询关键词
    返回匹配的手册内容和文件信息
    """
    try:
        # 1. 初始化Embedding模型（全局初始化更好，这里为演示简化）
        embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
        )
        
        # 2. 加载向量库和映射
        vector_store, id_map = load_index_and_map(
            embedding_model, 
            SHOUCE_INDEX_PATH, 
            ID_MAP_PATH
        )
        
        if not vector_store or not id_map:
            raise HTTPException(
                status_code=503, 
                detail="操作手册向量库未初始化，请先构建索引"
            )
 
        # 3. 执行相似度搜索
        search_results = vector_store.similarity_search(query, k=1)
        if not search_results:
            return ManualResponse(
                query=query,
                manual_content=None,
                filename="",
                scope_text="",
                error=f"未找到与'{query}'相关的内容"
            )
 
        # 4. 获取最佳匹配结果
        best_match = search_results[0]
        doc_id = best_match.metadata.get("doc_id")
        filename = id_map.get(doc_id, "未知文件")
        scope_text = best_match.page_content
 
        # 5. 查找Markdown文件
        md_path = find_markdown_file(MARKDOWN_ROOT_FOLDER, filename)
        if not md_path:
            return ManualResponse(
                query=query,
                manual_content=None,
                filename=filename,
                scope_text=scope_text,
                error="找到匹配手册但未找到对应的Markdown文件"
            )
 
        # 6. 读取文件内容
        images = collect_manual_images(md_path)
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
 
        return ManualResponse(
            query=query,
            manual_content=content,
            filename=filename,
            scope_text=scope_text,
            images=images
        )
 
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"查询操作手册时发生错误: {str(e)}"
        )
    
    
@app.get("/", summary="服务状态检查")
def read_root():
    """
    根路径，用于检查API服务是否正常运行。
    """
    return {
        "message": "RAG知识库API服务正在运行。",
        "current_docs_count": len(all_splits),
        "index_path": INDEX_PATH,
        "splits_file": SPLITS_FILE
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server2:app", host="0.0.0.0", port=8000, reload=True)
