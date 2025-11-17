import os
import json
import uuid
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from config import JSON_DATA_PATH,MARKDOWN_ROOT_FOLDER,SHOUCE_INDEX_PATH,ID_MAP_PATH,EMBEDDING_MODEL_NAME


def load_manual_data(json_path: str) -> dict:
    """从JSON文件加载文件名及其适用范围的映射关系"""
    if not os.path.exists(json_path):
        print(f"错误: JSON数据文件未找到: {json_path}")
        return {}
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_vector_store(manual_data: dict, embedding_model):
    """根据手册数据创建FAISS向量库和ID映射"""
    documents = []
    id_to_filename_map = {}

    for filename, scope_text in manual_data.items():
        if not isinstance(scope_text, str) or not scope_text.strip():
            continue
        
        # 为每个适用范围创建一个Document对象
        # page_content是用于embedding和检索的文本
        # metadata用于存储我们需要的信息，这里主要是原始ID和文件名
        doc_id = str(uuid.uuid4())
        doc = Document(
            page_content=scope_text,
            metadata={"filename": filename, "doc_id": doc_id}
        )
        documents.append(doc)
        id_to_filename_map[doc_id] = filename

    if not documents:
        print("警告: 没有找到有效的文档数据来创建向量库。")
        return None, None

    vector_store = FAISS.from_documents(documents, embedding_model)
    return vector_store, id_to_filename_map

def save_index_and_map(vector_store, id_map, index_path, map_path):
    """保存FAISS索引和ID映射到本地"""
    os.makedirs(index_path, exist_ok=True)
    vector_store.save_local(index_path)
    with open(map_path, 'w', encoding='utf-8') as f:
        json.dump(id_map, f, ensure_ascii=False, indent=4)
    print(f"向量库和ID映射已保存至 '{index_path}' 和 '{map_path}'")

def load_index_and_map(embedding_model, index_path, map_path):
    """从本地加载FAISS索引和ID映射"""
    if not os.path.exists(index_path) or not os.path.exists(map_path):
        return None, None
    try:
        vector_store = FAISS.load_local(index_path, embeddings=embedding_model, allow_dangerous_deserialization=True)
        with open(map_path, 'r', encoding='utf-8') as f:
            id_map = json.load(f)
        print("成功加载本地向量库和ID映射。")
        return vector_store, id_map
    except Exception as e:
        print(f"加载本地索引失败: {e}")
        return None, None

def find_markdown_file(root_folder: str, target_filename: str) -> str | None:
    """通过模糊匹配在指定文件夹的子文件夹中查找markdown文件"""
    # 去掉可能的.docx后缀，只获取核心文件名用于匹配
    # 例如，从 "零星需求操作指导书.docx" 得到 "零星需求操作指导书"
    core_name_to_match = os.path.splitext(target_filename)[0]

    if not os.path.isdir(root_folder):
        return None

    # 遍历父文件夹下的所有子文件夹
    for sub_folder_name in os.listdir(root_folder):
        sub_folder_path = os.path.join(root_folder, sub_folder_name)
        
        # 确保它是一个文件夹
        if os.path.isdir(sub_folder_path):
            # 检查子文件夹名是否包含目标核心文件名（不区分大小写）
            if core_name_to_match.lower() in sub_folder_name.lower():
                # 如果匹配成功，就在这个子文件夹中查找.md文件
                for file_name in os.listdir(sub_folder_path):
                    if file_name.endswith(".md"):
                        return os.path.join(sub_folder_path, file_name)
                
    # 如果遍历完所有子文件夹都没有找到匹配的
    return None

def search_and_return_manual(query: str, vector_store, id_map, markdown_root_folder):
    """执行搜索并返回找到的markdown文件内容"""
    # 1. 使用FAISS进行相似度搜索
    # k=1 表示我们只想要最匹配的那一个结果
    search_results = vector_store.similarity_search(query, k=1)
    
    if not search_results:
        print(f"未找到与查询 '{query}' 相关的手册。")
        return

    # 2. 从结果中获取最相关文档的元数据
    best_match_doc = search_results[0]
    doc_id = best_match_doc.metadata.get("doc_id")
    
    if not doc_id or doc_id not in id_map:
        print("错误: 无法从搜索结果中定位到原始文件名。")
        return

    # 3. 通过ID映射找到原始的文件名
    original_filename = id_map[doc_id]
    print(f"查询: '{query}'")
    print(f"匹配到的适用范围: '{best_match_doc.page_content}'")
    print(f"关联的手册文件名: '{original_filename}'")

    # 4. 在文件夹中查找对应的Markdown文件
    md_file_path = find_markdown_file(markdown_root_folder, original_filename)
    
    if md_file_path:
        print(f"成功找到Markdown文件: {md_file_path}\n")
        print("--- Markdown文件内容如下 ---")
        try:
            with open(md_file_path, "r", encoding="utf-8") as f:
                content = f.read()
                print(content)
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
    else:
        print(f"在文件夹 '{markdown_root_folder}' 中未找到与 '{original_filename}' 对应的Markdown文件。")


if __name__ == "__main__":
    # 1. 初始化Embedding模型
    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    # 2. 检查是否存在已构建的索引，如果没有则创建
    vector_store, id_map = load_index_and_map(embedding_model, SHOUCE_INDEX_PATH, ID_MAP_PATH)

    if vector_store is None or id_map is None:
        print("本地未找到索引，开始从JSON数据创建...")
        manual_data = load_manual_data(JSON_DATA_PATH)
        vector_store, id_map = create_vector_store(manual_data, embedding_model)
        
        if vector_store and id_map:
            save_index_and_map(vector_store, id_map, SHOUCE_INDEX_PATH, ID_MAP_PATH)
        else:
            exit() # 创建失败，退出


    user_query = "零部件"
    
    # 检查markdown文件夹是否存在
    if not os.path.isdir(MARKDOWN_ROOT_FOLDER):
        print(f"错误: Markdown文件夹路径无效或不存在: {MARKDOWN_ROOT_FOLDER}")
        print("请将 MARKDOWN_ROOT_FOLDER 变量设置为正确的路径。")
    else:
        search_and_return_manual(user_query, vector_store, id_map, MARKDOWN_ROOT_FOLDER)