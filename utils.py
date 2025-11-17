from datetime import datetime
from langchain_core.messages import AIMessage
import os
import re
import shutil
from pathlib import Path
import uuid
import os
import json
import uuid
import shutil
from typing import Dict, List, Optional
import re
import pymysql
# --- 从原文件导入必要的类和函数 ---
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from rank_bm25 import BM25Okapi
from config import BASE_DATA_DIR,DEPARTMENTS_DIR,VECTOR_STORES_DIR,vector_stores
from fastapi import  UploadFile
from common.mysql import get_db_connection
with open('common/prompts.json', 'r', encoding='utf-8') as f:
    PROMPT_CONFIG = json.load(f)

# --- 配置常量 (与原文件保持一致) ---
INDEX_PATH = "faiss_index_only"
SPLITS_FILE = "splits_data.json"
EMBEDDING_MODEL_NAME = "BAAI/bge-small-zh-v1.5"
BM25_CORPUS_FILE = "bm25_corpus_data.json"

embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL_NAME,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

def extract_ai_response(messages):
    """
    从消息列表中提取 AI 回复的内容。

    参数:
    messages (list): 包含 HumanMessage 和 AIMessage 对象的列表。

    返回:
    str: AI 回复的内容，如果没有找到 AIMessage 对象，则返回 None。
    """
    for message in messages:
        if isinstance(message, AIMessage):
            return message.content
    return None

def rename_markdown_files(data_dir):
    """
    递归批量重命名markdown文件，根据父目录名重命名.md文件
    支持多层嵌套目录结构，处理类似 full.md 或其他原始文件名的情况

    Args:
        data_dir (str): data目录的路径
    """
    from pathlib import Path
    import re

    data_path = Path(data_dir)

    if not data_path.exists():
        print(f"错误：目录 '{data_dir}' 不存在")
        return

    renamed_count = 0
    error_count = 0

    # 正则表达式匹配UUID格式（8-4-4-4-12的十六进制数字）和.pdf后缀
    uuid_pattern = r'-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
    pdf_pattern = r'\.pdf$'

    # 使用rglob递归查找所有.md文件
    for md_file in data_path.rglob("*.md"):
        try:
            # 获取父目录名
            parent_dir_name = md_file.parent.name
            
            # 清理父目录名：移除UUID和.pdf后缀
            clean_name = re.sub(uuid_pattern, '', parent_dir_name, flags=re.IGNORECASE)
            clean_name = re.sub(pdf_pattern, '', clean_name, flags=re.IGNORECASE)
            
            # 如果清理后的名字为空，则保留原始文件名
            if not clean_name.strip():
                clean_name = md_file.stem

            # 新文件名
            new_filename = clean_name + ".md"
            new_filepath = md_file.parent / new_filename

            # 如果新旧文件名相同，跳过
            if new_filepath == md_file:
                print(f"跳过：'{md_file.relative_to(data_path)}' 无需重命名")
                continue

            # 处理文件名冲突
            counter = 1
            temp_new_filepath = new_filepath
            while temp_new_filepath.exists():
                temp_new_filename = f"{clean_name}_{counter}.md"
                temp_new_filepath = md_file.parent / temp_new_filename
                counter += 1

            # 重命名文件
            md_file.rename(temp_new_filepath)
            print(f"成功：'{md_file.relative_to(data_path)}' -> '{temp_new_filepath.name}'")
            renamed_count += 1

        except Exception as e:
            print(f"错误：重命名 '{md_file.relative_to(data_path)}' 失败 - {str(e)}")
            error_count += 1

    print(f"\n完成！成功重命名 {renamed_count} 个文件，失败 {error_count} 个文件")

def parse_date_from_text(s: str):
    """尝试从字符串中解析常见日期格式，返回 ISO 日期字符串（YYYY-MM-DD）或 None。
    优先匹配：YYYY年M月D日、YYYY年M月、YYYY[./-]MM[./-]DD 或 YYYY[./-]MM
    如果只有年+月，则返回该月第一天的 ISO 日期（YYYY-MM-01）。"""
    if not s:
        return None
    s = s.strip()
    # 形如 2014年4月10日 或 2014年4月
    m = re.search(r'(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日', s)
    if m:
        y, mo, d = m.groups()
        try:
            return datetime(int(y), int(mo), int(d)).date().isoformat()
        except Exception:
            pass
    m = re.search(r'(\d{4})\s*年\s*(\d{1,2})\s*月', s)
    if m:
        y, mo = m.groups()
        try:
            return datetime(int(y), int(mo), 1).date().isoformat()
        except Exception:
            pass
    # 形如 2014.4.10 or 2014-04-10 or 2014/04/10
    m = re.search(r'(\d{4})[./-](\d{1,2})[./-](\d{1,2})', s)
    if m:
        y, mo, d = m.groups()
        try:
            return datetime(int(y), int(mo), int(d)).date().isoformat()
        except Exception:
            pass
    # 形如 2014-04 or 2014.04
    m = re.search(r'(\d{4})[./-](\d{1,2})', s)
    if m:
        y, mo = m.groups()
        try:
            return datetime(int(y), int(mo), 1).date().isoformat()
        except Exception:
            pass
    # 最后尝试仅提取年份（不推荐）
    m = re.search(r'\b(19|20)\d{2}\b', s)
    if m:
        y = m.group(0)
        try:
            return datetime(int(y), 1, 1).date().isoformat()
        except Exception:
            pass
    return None

def chunk_md_content(content: str, source_filename: str) -> List[Document]:
    """
    对单个markdown文件内容进行切分。
    """
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=False)
    md_header_splits = markdown_splitter.split_text(content)
    new_docs = []
    for doc in md_header_splits:
        page_content = re.sub(r'\(.*?images.*?\)', '', doc.page_content)
        page_content = re.sub(r'\s+', ' ', page_content).strip()
        if len(page_content) < 30:
            continue
        source = source_filename.replace(".md", "")
        text_to_embed = f"来源: {source} 内容: {page_content}"
        new_metadata = doc.metadata.copy() if hasattr(doc, 'metadata') and doc.metadata else {}
        new_metadata.update({
            "source": source,
            "id": str(uuid.uuid4())
        })
        new_metadata['original_content'] = page_content
        new_docs.append(Document(page_content=text_to_embed, metadata=new_metadata))
    return new_docs

def load_existing_data():
    """启动时加载现有的向量库和切分数据"""
    global vector_store, all_splits
    print("启动中：尝试加载现有知识库...")
    index_file_path = os.path.join(INDEX_PATH, "index.faiss")
    if os.path.exists(index_file_path) and os.path.exists(SPLITS_FILE) and os.path.exists(BM25_CORPUS_FILE):
        try:
            vector_store = FAISS.load_local(INDEX_PATH, embeddings=embedding_model, allow_dangerous_deserialization=True)
            all_splits = load_splits_from_file(SPLITS_FILE)
            with open(BM25_CORPUS_FILE, 'r', encoding='utf-8') as f:
                loaded_corpus = json.load(f)
            bm25_corpus = [[str(token) for token in doc_tokens] for doc_tokens in loaded_corpus]
            bm25_instance = BM25Okapi(bm25_corpus)
            print("知识库加载成功。")
        except Exception as e:
            print(f"加载失败: {e}。将初始化为空知识库。")
            vector_store = None
            all_splits = []
    else:
        print("未找到现有知识库，将初始化为空。")
        vector_store = None
        all_splits = []
    return vector_store,all_splits,bm25_instance

def save_all_data():
    """将当前的内存数据持久化到磁盘"""
    if not all_splits:
        print("没有数据可保存。")
        return
    print("保存知识库和切分数据...")
    os.makedirs(INDEX_PATH, exist_ok=True)
    if vector_store:
        vector_store.save_local(INDEX_PATH)
    save_splits_to_file(all_splits, SPLITS_FILE)
    print("保存完成。")

def load_splits_from_file(file_path: str) -> List[Document]:
    """从JSON文件加载切分后的Document对象列表"""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    loaded_splits = []
    for doc_dict in data:
        page_content = doc_dict.get('page_content', '')
        metadata = doc_dict.get('metadata', {})
        loaded_splits.append(Document(page_content=page_content, metadata=metadata))
    return loaded_splits

def save_splits_to_file(splits: List[Document], file_path: str):
    """将Document对象列表序列化并保存到JSON文件"""
    def default_serializer(obj):
        if isinstance(obj, Document):
            return obj.__dict__
        return str(obj)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(splits, f, default=default_serializer, ensure_ascii=False, indent=2)

def message_change(results,query):
    context_parts = []
    
    for result in results:
        content = result["content"]
        source = result["source"]
        context_parts.append(f"【来源: {source}】\n{content}")

        # 添加上下文段落（如果存在）
        for context_item in result.get("context", []):
            context_content = context_item["content"]
            context_source = context_item["source"]
            context_parts.append(f"【相关上下文 - 来源: {context_source}】\n{context_content}")

    # 4. 构建消息并调用API
    system_prompt = PROMPT_CONFIG["answer_generator"]["system_prompt"]

    messages = [{"role": "system", "content": system_prompt}]
    full_context = "\n\n".join(context_parts)
    # 添加上下文和当前问题 - 这里将检索到的内容传递给AI
    user_message = f"基于以下检索到的文档内容回答问题：\n\n{full_context}\n\n问题：{query}"
    print(user_message)
    messages.append({"role": "user", "content": user_message})
    return messages

def ensure_department_exists(department_name: str):
    """
    如果部门不存在，则动态创建它。
    包括：1. 在MySQL中添加部门记录；2. 创建文件夹；3. 准备向量库。
    """
    # 1. 检查并创建数据库记录（如果不存在）
    # 此处需要一个辅助函数来查询和插入部门
    if not department_exists_in_db(department_name):
        create_department_in_db(department_name)
 
    # 2. 检查并创建文件系统目录
    department_folder = DEPARTMENTS_DIR / department_name
    department_folder.mkdir(parents=True, exist_ok=True)
 
    # 3. 检查并加载向量库（如果不存在，则由后续逻辑创建）
    # 此函数不直接创建FAISS实例，因为需要文档内容。
    # 但它会确保路径存在，并将部门名称添加到全局字典中以备后续使用。
    if department_name not in vector_stores:
        # 尝试从磁盘加载已存在的向量库
        vector_store_path = VECTOR_STORES_DIR / f"{department_name}.faiss"
        if vector_store_path.exists():
            print(f"为已存在部门 '{department_name}' 加载向量库...")
            vector_stores[department_name] = FAISS.load_local(str(vector_store_path), embedding_model, allow_dangerous_deserialization=True)


def pdf_to_markdown(pdf_file: UploadFile, save_path: Path) -> Path:
    """将上传的PDF文件转换为Markdown并保存"""
    # try:
    #     pdf_content = pdf_file.file.read()
    #     doc = fitz.open(stream=pdf_content, filetype="pdf")
    #     markdown_text = ""
    #     for page in doc:
    #         markdown_text += page.get_text()
        
    #     with open(save_path, "w", encoding="utf-8") as f:
    #         f.write(markdown_text)
    #     return save_path
    # except Exception as e:
    #     raise Exception(f"PDF转换失败: {e}")

def save_all_department_vector_stores(vector_stores: Dict[str, FAISS]):
    """
    安全地保存所有部门向量库到磁盘。
    此函数会为每个部门创建一个独立的目录，并在其中保存 FAISS 索引文件。
    这可以解决因目录不存在（尤其是新部门）而导致的保存失败问题。
 
    :param vector_stores: 包含部门名和对应FAISS向量库的字典。
    """
    for dept_name, vector_store in vector_stores.items():
        # 1. 构建该部门专属的存储目录路径
        dept_store_path = DEPARTMENTS_DIR / dept_name
        
        # 2. 确保目录存在。如果不存在，则递归创建所有父目录。
        dept_store_path.mkdir(parents=True, exist_ok=True)
        
        # 3. 将向量库保存到这个目录中
        # FAISS的 save_local 方法会自动在该目录下创建 index.faiss 和 index.pkl 文件
        vector_store.save_local(str(dept_store_path))

def load_vector_store_if_exists(department_name: str, embedding_model) -> FAISS | None:
    """
    如果向量库文件存在，则加载并返回FAISS实例；否则返回None。
    """
    vector_store_path = VECTOR_STORES_DIR / f"{department_name}.faiss"
    if vector_store_path.exists():
        print(f"为已存在部门 '{department_name}' 加载向量库...")
        return FAISS.load_local(
            str(vector_store_path), 
            embedding_model, 
            allow_dangerous_deserialization=True
        )
    return None

def department_exists_in_db(department_name: str) -> bool:
    """检查部门是否存在于数据库中"""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT 1 FROM departments WHERE name = %s LIMIT 1"
                cursor.execute(sql, (department_name,))
                return cursor.fetchone() is not None
    except pymysql.Error as e:
        print(f"数据库查询错误: {e}")
        return False
 
def create_department_in_db(department_name: str) -> Optional[int]:
    """在数据库中创建新部门，返回新创建的部门ID"""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                sql = "INSERT INTO departments (name) VALUES (%s)"
                cursor.execute(sql, (department_name,))
                conn.commit()
                return cursor.lastrowid
    except pymysql.Error as e:
        print(f"数据库插入错误: {e}")
        return None

def load_all_department_vector_stores(embedding_model):
    loaded_stores = {}
    indexes_dir = Path("data/vector_stores") # 假设你的索引都保存在这里
    
    if not indexes_dir.exists():
        print("向量库索引目录不存在，将在首次上传文档时创建。")
        return {}
 
    for item in indexes_dir.iterdir():
        # 假设部门名就是文件夹名，例如 "data/vector_stores/销售部"
        if item.is_dir():
            department_name = item.name
            try:
                # 加载该部门的FAISS索引
                store = FAISS.load_local(item, embedding_model, allow_dangerous_deserialization=True)
                loaded_stores[department_name] = store
                print(f"成功加载部门 '{department_name}' 的向量库。")
            except Exception as e:
                print(f"加载部门 '{department_name}' 的向量库失败: {e}")
    return loaded_stores