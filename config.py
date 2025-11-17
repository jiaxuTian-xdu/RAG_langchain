# 存储操作手册信息的JSON文件路径
from pathlib import Path


JSON_DATA_PATH = "./word2md/适用范围总结.json"  # 假设您的JSON文件名为 manuals.json
# 存储Markdown操作手册文档的根文件夹
MARKDOWN_ROOT_FOLDER = "word2md" # 请将此路径替换为您实际的Markdown文件夹路径
# FAISS向量库索引和ID映射文件的存储目录
SHOUCE_INDEX_PATH = "faiss_manual_index"
INDEX_PATH = "faiss_index_only"

ID_MAP_PATH = "id_to_filename_map.json"
# 使用的Embedding模型
EMBEDDING_MODEL_NAME = "BAAI/bge-small-zh-v1.5"

SPLITS_FILE = "splits_data.json"
BM25_CORPUS_FILE = "bm25_corpus_data.json"

#数据库配置文件
BASE_DATA_DIR = Path("./data") 
DEPARTMENTS_DIR = BASE_DATA_DIR / "departments"
VECTOR_STORES_DIR = BASE_DATA_DIR / "vector_stores"
vector_stores = {} 
DEPARTMENTS_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_STORES_DIR.mkdir(parents=True, exist_ok=True)