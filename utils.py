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
from typing import List
import re
# --- 从原文件导入必要的类和函数 ---
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from rank_bm25 import BM25Okapi


# --- 配置常量 (与原文件保持一致) ---
INDEX_PATH = "faiss_index_only"
SPLITS_FILE = "splits_data.json"
EMBEDDING_MODEL_NAME = "embedding_model"
BM25_CORPUS_FILE = "bm25_corpus_data.json"

embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL_NAME,
    model_kwargs={"device": "cuda"},
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