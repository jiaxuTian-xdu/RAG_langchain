import os
import json
import uuid
import re
from typing import List, Dict, Any
from openai import OpenAI

from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from utils import rename_markdown_files

# 初始化DeepSeek客户端
client = OpenAI(
    api_key="DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com"
)


class ConversationManager:
    """对话管理器，维护多轮对话历史"""

    def __init__(self, max_history_turns: int = 10):
        self.history = []
        self.max_history_turns = max_history_turns

    def add_message(self, role: str, content: str):
        """添加消息到对话历史"""
        self.history.append({"role": role, "content": content})

        # 保持历史长度不超过最大值
        if len(self.history) > self.max_history_turns * 2:  # 每轮有user和assistant两条
            self.history = self.history[-self.max_history_turns * 2:]

    def get_history(self) -> List[Dict[str, str]]:
        """获取对话历史"""
        return self.history.copy()

    def clear_history(self):
        """清空对话历史"""
        self.history = []


class QueryAnalyzer:
    """问题分析器，分解用户问题并生成关键词"""

    def __init__(self):
        self.system_prompt = """你是一个专业的问题分析助手。你的任务是将用户的问题分解成多个可以在知识库中搜索的关键词或子问题。

要求：
1. 分析用户问题的核心意图和关键信息点
2. 将复杂问题拆解成2-4个简单的子问题或关键词
3. 确保关键词能够有效地在文档库中进行检索
4. 对于需要多步推理的问题，拆解成逻辑步骤

返回格式要求：
以JSON格式返回，包含以下字段：
- "main_intent": 主要意图的简要描述
- "sub_queries": 子问题或关键词列表，每个元素是一个字符串
- "search_strategy": 搜索策略描述

示例：
用户问题："挂科对保研和奖学金有什么影响？"
返回：
{
  "main_intent": "了解挂科对保研和奖学金的影响",
  "sub_queries": ["挂科后果", "保研条件", "奖学金评定标准", "挂科记录处理"],
  "search_strategy": "先查找挂科的一般后果，再分别查找保研和奖学金的具体要求"
}"""

    def analyze_query(self, query: str, conversation_history: List[Dict] = None) -> Dict[str, Any]:
        """分析用户问题并生成搜索关键词"""
        try:
            # 构建对话历史上下文
            messages = [{"role": "system", "content": self.system_prompt}]

            # 如果有对话历史，添加最近几轮作为上下文
            if conversation_history:
                # 只取最近3轮对话作为上下文
                recent_history = conversation_history[-6:]  # 3轮对话（每轮2条消息）
                messages.extend(recent_history)

            # 添加当前问题
            messages.append({"role": "user", "content": f"请分析以下问题：{query}"})

            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                max_tokens=800,
                stream=False,
                temperature=0.1
            )

            result_text = response.choices[0].message.content

            # 尝试解析JSON
            try:
                # 提取JSON部分（有时AI会在JSON前后添加说明文字）
                json_match = re.search(r'\{.*\}', result_text, re.DOTALL)
                if json_match:
                    result_json = json.loads(json_match.group())
                else:
                    result_json = json.loads(result_text)

                # 验证必需字段
                if "main_intent" not in result_json or "sub_queries" not in result_json:
                    raise ValueError("缺少必需字段")

                return result_json

            except (json.JSONDecodeError, ValueError) as e:
                # 如果JSON解析失败，使用备用方案
                print(f"JSON解析失败，使用备用方案: {e}")
                return {
                    "main_intent": query,
                    "sub_queries": self._fallback_keyword_extraction(query),
                    "search_strategy": "直接搜索相关问题",
                    "raw_response": result_text
                }

        except Exception as e:
            print(f"问题分析失败: {e}")
            return {
                "main_intent": query,
                "sub_queries": self._fallback_keyword_extraction(query),
                "search_strategy": "直接搜索原问题",
                "error": str(e)
            }

    def _fallback_keyword_extraction(self, query: str) -> List[str]:
        """备用关键词提取方法"""
        # 简单的基于规则的关键词提取
        words = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z]+', query)
        # 过滤停用词（简单版本）
        stop_words = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很',
                      '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这'}
        keywords = [word for word in words if word not in stop_words and len(word) > 1]

        # 如果关键词太少，返回原问题作为唯一查询
        if len(keywords) < 2:
            return [query]

        return keywords[:4]  # 最多返回4个关键词


def read_markdown(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def find_md_files(root_folder: str) -> list:
    """
    递归查找指定文件夹中的所有.md文件
    """
    rename_markdown_files(root_folder)
    md_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                md_files.append(full_path)
    return md_files


def chunk_md_files(md_files: list) -> list:
    """
    处理所有.md文件，切分内容并标明来源
    """
    all_splits = []
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=False)

    for file_path in md_files:
        content = read_markdown(file_path)
        md_header_splits = markdown_splitter.split_text(content)
        for doc in md_header_splits:
            page_content = re.sub(r'\(.*?images.*?\)', '', doc.page_content)
            page_content = re.sub(r'\s+', ' ', page_content).strip()
            if len(page_content) < 30:
                continue

            source = os.path.basename(file_path).replace(".md", "")

            # 准备用于嵌入的文本，包含内容和来源
            text_to_embed = f"来源: {source} 内容: {page_content}"
            # 保留所有原始元数据，并确保id存在
            new_metadata = doc.metadata.copy() if hasattr(doc, 'metadata') and doc.metadata else {}
            new_metadata.update({
                "source": source,
                "file_path": file_path,  # 添加文件路径
                "id": str(uuid.uuid4())
            })

            # 存储原始内容，方便后续展示
            new_metadata['original_content'] = page_content

            all_splits.append(Document(page_content=text_to_embed, metadata=new_metadata))

    return all_splits


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


def call_deepseek_api(messages: List[Dict[str, str]], max_tokens: int = 2000) -> str:
    """
    调用DeepSeek API进行问答

    Args:
        messages: 消息列表，包含角色和内容
        max_tokens: 最大返回token数

    Returns:
        str: API返回的回答内容
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            max_tokens=max_tokens,
            stream=False,
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"调用DeepSeek API时出错: {str(e)}"


class KnowledgeBaseSystem:
    """知识库系统，整合搜索、对话和问题分析功能"""

    def __init__(self, vector_store, all_splits):
        self.vector_store = vector_store
        self.all_splits = all_splits
        self.conversation = ConversationManager()
        self.query_analyzer = QueryAnalyzer()

    def search_with_keywords(self, keywords: List[str], k_per_keyword: int = 2) -> List[Document]:
        """使用多个关键词进行搜索，合并结果"""
        all_docs = []

        for keyword in keywords:
            try:
                docs = self.vector_store.similarity_search(keyword, k=k_per_keyword)
                all_docs.extend(docs)
            except Exception as e:
                print(f"关键词 '{keyword}' 搜索失败: {e}")

        # 去重
        seen_ids = set()
        unique_docs = []
        for doc in all_docs:
            doc_id = doc.metadata['id']
            if doc_id not in seen_ids:
                seen_ids.add(doc_id)
                unique_docs.append(doc)

        return unique_docs

    def get_context_for_doc(self, doc: Document, context_range: int = 5) -> str:
        """获取文档的上下文内容"""
        # 找到当前doc在all_splits中的索引
        index = next((i for i, d in enumerate(self.all_splits) if d.metadata['id'] == doc.metadata['id']), None)
        if index is None:
            return doc.metadata.get('original_content', doc.page_content)

        # 获取文件路径并读取文件内容
        file_path = doc.metadata.get('file_path')
        if file_path and os.path.exists(file_path):
            file_content = read_markdown(file_path)
            file_word_count = len(file_content)

            if file_word_count < 5000:
                # 文件字数小于5000，使用整个文件内容
                return file_content
            else:
                # 文件字数大于5000，使用chunk附近context_range个chunk
                start_index = max(0, index - context_range)
                end_index = min(len(self.all_splits), index + context_range + 1)
                context_docs = self.all_splits[start_index:end_index]

                # 拼接附近chunk的内容
                context_content = "\n\n".join([
                    context_doc.metadata.get('original_content', context_doc.page_content)
                    for context_doc in context_docs
                ])
                return context_content
        else:
            # 如果找不到文件路径，使用附近chunk
            start_index = max(0, index - context_range)
            end_index = min(len(self.all_splits), index + context_range + 1)
            context_docs = self.all_splits[start_index:end_index]
            context_content = "\n\n".join([
                context_doc.metadata.get('original_content', context_doc.page_content)
                for context_doc in context_docs
            ])
            return context_content

    def process_query(self, query: str, k_per_keyword: int = 2, context_range: int = 3) -> Dict[str, Any]:
        """处理用户查询的完整流程"""
        print(f"\n🔍 分析问题: {query}")

        # 1. 分析问题并生成关键词
        analysis_result = self.query_analyzer.analyze_query(
            query,
            self.conversation.get_history()
        )

        print(f"📝 主要意图: {analysis_result['main_intent']}")
        print(f"🔑 搜索关键词: {analysis_result['sub_queries']}")
        print(f"🎯 搜索策略: {analysis_result.get('search_strategy', 'N/A')}")

        # 2. 使用关键词搜索
        relevant_docs = self.search_with_keywords(analysis_result['sub_queries'], k_per_keyword)

        if not relevant_docs:
            result = {
                "query": query,
                "analysis": analysis_result,
                "error": "未找到相关文档",
                "answer": "抱歉，我没有找到与您问题相关的信息。请尝试换一种方式提问。"
            }

            # 添加到对话历史
            self.conversation.add_message("user", query)
            self.conversation.add_message("assistant", result["answer"])

            return result

        # 3. 获取上下文内容
        context_parts = []
        for doc in relevant_docs:
            context_content = self.get_context_for_doc(doc, context_range)
            source = doc.metadata['source']
            context_parts.append(f"【来源: {source}】\n{context_content}")

        full_context = "\n\n".join(context_parts)

        # 4. 构建消息并调用API
        system_prompt = """你是一个专业的问答助手，基于提供的上下文内容回答用户问题。

要求：
1. 严格基于上下文内容提供准确回答
2. 如果上下文中有相关信息，请引用并说明来源
3. 如果上下文中没有足够信息，请如实告知
4. 结合对话历史理解用户意图
5. 回答要简洁明了，重点突出
6. 如果用户问题涉及多个方面，请分别回答"""

        messages = [{"role": "system", "content": system_prompt}]

        # 添加对话历史
        messages.extend(self.conversation.get_history())

        # 添加上下文和当前问题
        user_message = f"上下文内容：\n{full_context}\n\n当前问题：{query}"
        messages.append({"role": "user", "content": user_message})

        # 调用API
        ai_answer = call_deepseek_api(messages)

        # 5. 构建结果
        result = {
            "query": query,
            "analysis": analysis_result,
            "matched_sources": list(set([doc.metadata['source'] for doc in relevant_docs])),
            "total_documents": len(relevant_docs),
            "context_length": len(full_context),
            "answer": ai_answer,
            "documents_details": [
                {
                    "source": doc.metadata['source'],
                    "content_preview": doc.metadata.get('original_content', doc.page_content)[:100] + "...",
                    "file_path": doc.metadata.get('file_path', 'N/A')
                }
                for doc in relevant_docs
            ]
        }

        # 6. 更新对话历史
        self.conversation.add_message("user", query)
        self.conversation.add_message("assistant", ai_answer)

        return result


def initialize_search_system(root_folder="data", index_path="save/faiss_index_only",
                             splits_file="save/splits_data.json"):
    """
    初始化搜索系统

    Returns:
        tuple: (vector_store, all_splits, embedding) 向量库、所有切分、嵌入模型
    """
    embedding = HuggingFaceEmbeddings(
        model_name=".embedding_model",
        model_kwargs={"device": "cuda"},
        encode_kwargs={"normalize_embeddings": True}
    )

    index_file_path = os.path.join(index_path, "index.faiss")

    if os.path.exists(index_file_path) and os.path.exists(splits_file):
        print(f"加载本地FAISS索引和切分数据...")
        try:
            vector_store = FAISS.load_local(index_path, embeddings=embedding, allow_dangerous_deserialization=True)
            all_splits = load_splits(splits_file)
            print("加载成功")
        except Exception as e:
            print(f"加载失败: {e}")
            print("将重新创建索引...")
            os.makedirs(index_path, exist_ok=True)
            md_files = find_md_files(root_folder)
            all_splits = chunk_md_files(md_files)
            vector_store = FAISS.from_documents(all_splits, embedding)
            vector_store.save_local(index_path)
            save_splits(all_splits, splits_file)
            print("重新创建并保存完成")
    else:
        print(f"本地未找到索引文件或切分数据，开始处理文档并创建新索引...")
        md_files = find_md_files(root_folder)
        all_splits = chunk_md_files(md_files)

        output_file = "save/chunks_output.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            for i, doc in enumerate(all_splits):
                original_content = doc.metadata.get('original_content', doc.page_content)
                f.write(f"--- Chunk {i + 1} ---\n")
                f.write(f"Source: {doc.metadata['source']}\n")
                f.write(f"Content:\n{original_content}\n\n")
        print(f"切分结果已保存到: {output_file}")

        os.makedirs(index_path, exist_ok=True)
        vector_store = FAISS.from_documents(all_splits, embedding)
        vector_store.save_local(index_path)
        save_splits(all_splits, splits_file)
        print(f"FAISS索引和切分数据已保存到 {index_path} 和 {splits_file}")

    return vector_store, all_splits, embedding


def print_interactive_results(result):
    """以交互式格式打印结果"""
    print(f"\n{'=' * 80}")
    print(f"📋 问题分析结果")
    print(f"{'=' * 80}")
    print(f"🔍 用户问题: {result['query']}")
    print(f"🎯 主要意图: {result['analysis']['main_intent']}")
    print(f"🔑 搜索关键词: {', '.join(result['analysis']['sub_queries'])}")
    print(f"📚 找到文档: {result['total_documents']} 个")
    print(f"📖 来源文件: {', '.join(result['matched_sources'])}")
    print(f"📝 上下文长度: {result['context_length']} 字符")

    print(f"\n🤖 AI回答:")
    print(f"{'─' * 40}")
    print(result['answer'])
    print(f"{'─' * 40}")

    if 'documents_details' in result and result['documents_details']:
        print(f"\n📄 参考文档:")
        for i, doc in enumerate(result['documents_details']):
            print(f"  {i + 1}. {doc['source']}: {doc['content_preview']}")


def interactive_chat():
    """交互式聊天界面"""
    print("🚀 初始化知识库系统...")
    vector_store, all_splits, embedding = initialize_search_system()
    kb_system = KnowledgeBaseSystem(vector_store, all_splits)

    print("\n" + "=" * 60)
    print("🤖 知识库问答系统已启动!")
    print("输入 '退出' 或 'quit' 结束对话")
    print("输入 '清除' 或 'clear' 清除对话历史")
    print("=" * 60)

    while True:
        try:
            user_input = input("\n💬 请输入您的问题: ").strip()

            if user_input.lower() in ['退出', 'quit', 'exit']:
                print("👋 再见!")
                break
            elif user_input.lower() in ['清除', 'clear']:
                kb_system.conversation.clear_history()
                print("🗑️ 对话历史已清除")
                continue
            elif not user_input:
                continue

            # 处理查询
            result = kb_system.process_query(user_input)
            print_interactive_results(result)

        except KeyboardInterrupt:
            print("\n👋 用户中断，再见!")
            break
        except Exception as e:
            print(f"❌ 处理问题时出错: {e}")


if __name__ == "__main__":
    # 检查API密钥
    if not os.environ.get('DEEPSEEK_API_KEY'):
        print("⚠️  警告: 未设置 DEEPSEEK_API_KEY 环境变量")
        print("请设置环境变量: export DEEPSEEK_API_KEY='your_api_key_here'")

    # 启动交互式聊天
    interactive_chat()