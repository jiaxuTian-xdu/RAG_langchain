import os
import json
import re
import uuid
import numpy as np
import jieba  # <-- 1. 导入 jieba 库
 
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from rank_bm25 import BM25Okapi
from utils import rename_markdown_files, parse_date_from_text
def tokenize_text(text: str) -> list:
    """
    使用jieba库进行中文分词，用于BM25。
    这比按字符切分能提供更准确的语义匹配。
    """
    return jieba.lcut(text)
 
def chunk_md_files(md_files: list) -> tuple[list, list]:
    """
    处理所有.md文件，先按标题切分，再对长文本进行递归切分，并标明来源。
    同时创建用于BM25检索的语料库。
    
    返回:
        tuple: (all_splits, bm25_corpus)
    """
    all_splits = []
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=False)
    
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", "。", "！", "？", " ", ""]
    )
 
    for file_path in md_files:
        content = read_markdown(file_path)
        content_lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
        pub_date = None
        for ln in content_lines[:80]:  
            d = parse_date_from_text(ln)
            if d:
                pub_date = d
                break
                
        md_header_splits = markdown_splitter.split_text(content)
        for doc in md_header_splits:
            page_content = re.sub(r'\(.*?images.*?\)', '', doc.page_content)
            page_content = re.sub(r'\s+', ' ', page_content).strip()
            if len(page_content) < 30:
                continue
 
            if len(page_content) > 1000:
                sub_docs = recursive_splitter.create_documents([page_content])
                for sub_doc in sub_docs:
                    sub_content = sub_doc.page_content.strip()
                    if len(sub_content) < 30:
                        continue
 
                    source = os.path.basename(file_path).replace(".md", "")
                    text_to_embed = f"来源: {source} 内容: {sub_content}"
                    
                    new_metadata = doc.metadata.copy() if hasattr(doc, 'metadata') and doc.metadata else {}
                    new_metadata.update({
                        "source": source,
                        "id": str(uuid.uuid4()),
                        "date": pub_date,
                        "original_content": sub_content
                    })
                    all_splits.append(Document(page_content=text_to_embed, metadata=new_metadata))
            else:
                source = os.path.basename(file_path).replace(".md", "")
                text_to_embed = f"来源: {source} 内容: {page_content}"
                
                new_metadata = doc.metadata.copy() if hasattr(doc, 'metadata') and doc.metadata else {}
                new_metadata.update({
                    "source": source,
                    "id": str(uuid.uuid4()),
                    "date": pub_date,
                    "original_content": page_content
                })
                all_splits.append(Document(page_content=text_to_embed, metadata=new_metadata))
    
    # BM25应在原始内容上运行，而不是 "来源: xxx 内容: xxx" 的组合文本
    bm25_corpus = [tokenize_text(doc.metadata['original_content']) for doc in all_splits]
    
    return all_splits, bm25_corpus
 
def read_markdown(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content
 
def find_md_files(root_folder: str) -> list:
    rename_markdown_files(root_folder)
    md_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                md_files.append(full_path)
    return md_files
 
def save_splits(splits, file_path):
    def default_serializer(obj):
        if isinstance(obj, Document):
            return obj.__dict__
        return str(obj)
 
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(splits, f, default=default_serializer, ensure_ascii=False, indent=2)
 
def load_splits(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    loaded_splits = []
    for doc_dict in data:
        page_content = doc_dict.get('page_content', '')
        metadata = doc_dict.get('metadata', {})
        loaded_splits.append(Document(page_content=page_content, metadata=metadata))
        
    return loaded_splits
 
def search(vector_store, bm25, all_splits, query, k, context_range=2, semantic_weight=0.6, bm25_weight=0.4):
    tokenized_query = tokenize_text(query) 
    
    # 1. 语义检索
    semantic_docs = vector_store.similarity_search(query, k * 2)
    
    # 2. BM25 关键词检索
    bm25_scores = bm25.get_scores(tokenized_query)
    top_n_bm25_indices = np.argsort(bm25_scores)[::-1][:k * 2]
    bm25_docs = [all_splits[i] for i in top_n_bm25_indices]
    
    # 3. 融合与重排
    doc_scores = {}
    
    # 处理语义检索结果
    for i, doc in enumerate(semantic_docs):
        doc_id = doc.metadata['id']
        score = 1.0 / (i + 1)
        doc_scores[doc_id] = {
            'doc': doc,
            'score': score * semantic_weight
        }
    
    # 处理BM25检索结果
    for i, doc in enumerate(bm25_docs):
        doc_id = doc.metadata['id']
        bm25_score = bm25_scores[top_n_bm25_indices[i]]
        if doc_id in doc_scores:
            doc_scores[doc_id]['score'] += bm25_score * bm25_weight
        else:
            doc_scores[doc_id] = {
                'doc': doc,
                'score': bm25_score * bm25_weight
            }
 
    # 4. 按融合后的分数排序并取前k个
    sorted_docs = sorted(doc_scores.values(), key=lambda x: x['score'], reverse=True)
    final_relevant_docs = [item['doc'] for item in sorted_docs[:k]]
 
    # 5. 打印结果
    print(f"查询: {query}")
    print(f"混合检索后的前{k}个最相关段落及其上下文: (上下文范围: {context_range})")
    
    for doc in final_relevant_docs:
        original_content = doc.metadata.get('original_content', doc.page_content)
        source = doc.metadata['source']
        
        print(f"内容: {original_content}")
        print(f"来源: {source}")
        print("\n---\n")
        
        if context_range > 0:
            index = next((i for i, d in enumerate(all_splits) if d.metadata['id'] == doc.metadata['id']), None)
            if index is None:
                print(f"警告: 无法找到文档 {doc.metadata['id']} 在 all_splits 中的位置。")
                continue
            
            start_index = max(0, index - context_range)
            end_index = min(len(all_splits), index + context_range + 1)
            
            context_docs = all_splits[start_index:end_index]
            
            print(f"上下文段落 (共 {len(context_docs)} 个):")
            for context_doc in context_docs:
                if context_doc.metadata['id'] == doc.metadata['id']:
                    continue
                context_content = context_doc.metadata.get('original_content', context_doc.page_content)
                context_source = context_doc.metadata['source']
                print(f"内容: {context_content}")
                print(f"来源: {context_source}")
                print("\n---\n")
 
def hybrid_search(vector_store, bm25, all_splits, query, k, context_range=2, semantic_weight=0.6, bm25_weight=0.4):
    """
    执行混合检索（语义 + BM25），并返回格式化的结果。
    此函数专为 API 调用设计。
    """
    tokenized_query = tokenize_text(query) 

    # 1. 语义检索
    semantic_docs = vector_store.similarity_search(query, k * 2)

    # 2. BM25 关键词检索
    bm25_scores = bm25.get_scores(tokenized_query)
    top_n_bm25_indices = np.argsort(bm25_scores)[::-1][:k * 2]
    bm25_docs = [all_splits[i] for i in top_n_bm25_indices]

    # 3. 融合与重排
    doc_scores = {}

    # 处理语义检索结果
    for i, doc in enumerate(semantic_docs):
        doc_id = doc.metadata['id']
        # 使用简单的倒数作为相关性分数
        score = 1.0 / (i + 1) 
        doc_scores[doc_id] = {
            'doc': doc,
            'score': score * semantic_weight
        }

    # 处理BM25检索结果
    for i, doc in enumerate(bm25_docs):
        doc_id = doc.metadata['id']
        bm25_score = bm25_scores[top_n_bm25_indices[i]]
        if doc_id in doc_scores:
            doc_scores[doc_id]['score'] += bm25_score * bm25_weight
        else:
            doc_scores[doc_id] = {
                'doc': doc,
                'score': bm25_score * bm25_weight
            }

    # 4. 按融合后的分数排序并取前k个
    sorted_docs = sorted(doc_scores.values(), key=lambda x: x['score'], reverse=True)
    final_relevant_docs = [item['doc'] for item in sorted_docs[:k]]

    # 5. 格式化输出结果
    results = []
    for doc in final_relevant_docs:
        original_content = doc.metadata.get('original_content', doc.page_content)
        source = doc.metadata['source']
        doc_id = doc.metadata['id']

        result_item = {
            "content": original_content,
            "source": source,
            "context": []
        }
        
        if context_range > 0:
            try:
                index = next((i for i, d in enumerate(all_splits) if d.metadata['id'] == doc_id), None)
                if index is not None:
                    start_index = max(0, index - context_range)
                    end_index = min(len(all_splits), index + context_range + 1)
                    
                    for i in range(start_index, end_index):
                        # 跳过自身
                        if all_splits[i].metadata['id'] == doc_id:
                            continue
                        context_content = all_splits[i].metadata.get('original_content', all_splits[i].page_content)
                        context_source = all_splits[i].metadata['source']
                        result_item["context"].append({
                            "content": context_content,
                            "source": context_source
                        })
            except Exception as e:
                print(f"Error finding context for doc {doc_id}: {e}")
                # 可以选择添加一个错误提示，但保持 context 为空列表可能更友好
                # result_item["context"] = "无法获取上下文。"

        results.append(result_item)
        
    return results
 
if __name__ == "__main__":
    root_folder = "./MinerU"
    index_path = "faiss_index_only"
    splits_file = "splits_data.json"
    bm25_corpus_file = "bm25_corpus_data.json" 
 
    embedding = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-zh-v1.5",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
    
    index_file_path = os.path.join(index_path, "index.faiss")
    if os.path.exists(index_file_path) and os.path.exists(splits_file) and os.path.exists(bm25_corpus_file):
        print(f"加载本地FAISS索引、切分数据和BM25语料库...")
        try:
            vector_store = FAISS.load_local(index_path, embeddings=embedding, allow_dangerous_deserialization=True)
            all_splits = load_splits(splits_file)
            with open(bm25_corpus_file, 'r', encoding='utf-8') as f:
                loaded_corpus = json.load(f)
            bm25_corpus = [[str(token) for token in doc_tokens] for doc_tokens in loaded_corpus]
            bm25_instance = BM25Okapi(bm25_corpus)

            print("加载成功")
        except Exception as e:
            print(f"加载失败: {e}")
            print("将重新创建索引...")
            os.makedirs(index_path, exist_ok=True)
            md_files = find_md_files(root_folder)
            all_splits, bm25_corpus = chunk_md_files(md_files)
            bm25_instance = BM25Okapi(bm25_corpus)

            vector_store = FAISS.from_documents(all_splits, embedding)
            vector_store.save_local(index_path)
            save_splits(all_splits, splits_file)
            with open(bm25_corpus_file, 'w', encoding='utf-8') as f:
                json.dump(bm25_corpus, f, ensure_ascii=False)
            print("重新创建并保存完成")
    else:
        print(f"本地未找到索引文件或数据，开始处理文档并创建新索引...")
        md_files = find_md_files(root_folder)
        all_splits, bm25_corpus = chunk_md_files(md_files)
        bm25_instance = BM25Okapi(bm25_corpus)

        output_file = "chunks_output.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            for i, doc in enumerate(all_splits):
                original_content = doc.metadata.get('original_content', doc.page_content)
                f.write(f"--- Chunk {i+1} ---\n")
                f.write(f"Source: {doc.metadata['source']}\n")
                f.write(f"Content:\n{original_content}\n\n")
        print(f"切分结果已保存到: {output_file}")
 
        os.makedirs(index_path, exist_ok=True)
        vector_store = FAISS.from_documents(all_splits, embedding)
        vector_store.save_local(index_path)
        save_splits(all_splits, splits_file)
        with open(bm25_corpus_file, 'w', encoding='utf-8') as f:
            json.dump(bm25_corpus, f, ensure_ascii=False)
        print(f"FAISS索引、切分数据和BM25语料库已保存")
 
    query = "PSSA的目标是什么"
    k = 3
    context_range = 0  
    
    search(vector_store,bm25_instance, all_splits, query, k, context_range)
