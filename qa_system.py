import os
import json
import re
import uuid
from typing import List, Dict, Any
from openai import OpenAI

from langchain_core.documents import Document

# 初始化DeepSeek客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

# 加载提示词配置
with open('config/prompts.json', 'r', encoding='utf-8') as f:
    PROMPT_CONFIG = json.load(f)


class ConversationManager:
    """对话管理器，维护多轮对话历史"""

    def __init__(self, max_history_turns: int = 10):
        self.history = []
        self.max_history_turns = max_history_turns

    def add_message(self, role: str, content: str):
        """添加消息到对话历史"""
        self.history.append({"role": role, "content": content})

        # 保持历史长度不超过最大值
        if len(self.history) > self.max_history_turns * 2:
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
        self.system_prompt = PROMPT_CONFIG["query_analyzer"]["system_prompt"]

    def analyze_query(self, query: str, conversation_history: List[Dict] = None) -> Dict[str, Any]:
        """分析用户问题并生成搜索关键词"""
        try:
            # 构建对话历史上下文
            messages = [{"role": "system", "content": self.system_prompt}]

            # 如果有对话历史，添加最近几轮作为上下文
            if conversation_history:
                recent_history = conversation_history[-6:]
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
        words = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z]+', query)
        stop_words = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很',
                      '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这'}
        keywords = [word for word in words if word not in stop_words and len(word) > 1]

        if len(keywords) < 2:
            return [query]

        return keywords[:4]


class QASystem:
    """问答系统，整合检索和生成功能"""

    def __init__(self, vector_store, bm25_instance, all_splits):
        self.vector_store = vector_store
        self.bm25_instance = bm25_instance
        self.all_splits = all_splits
        self.conversation = ConversationManager()
        self.query_analyzer = QueryAnalyzer()

    def hybrid_search_documents(self, query: str, k: int = 3, context_range: int = 2,
                                semantic_weight: float = 0.6, bm25_weight: float = 0.4) -> List[Dict]:
        """
        使用混合检索获取相关文档
        直接调用chunks2中的hybrid_search函数
        """
        # 由于我们已经在chunks2模块中，可以直接调用
        from chunks import hybrid_search

        return hybrid_search(
            self.vector_store,
            self.bm25_instance,
            self.all_splits,
            query,
            k,
            context_range,
            semantic_weight,
            bm25_weight
        )

    def call_deepseek_api(self, messages: List[Dict[str, str]], max_tokens: int = 2000) -> str:
        """调用DeepSeek API进行问答"""
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

    def process_query(self, query: str, k: int = 3, context_range: int = 2) -> Dict[str, Any]:
        """处理用户查询的完整流程"""
        print(f"\n🔍 分析问题: {query}")

        # 1. 分析问题并生成关键词
        analysis_result = self.query_analyzer.analyze_query(
            query,
            self.conversation.get_history()
        )
        #
        # print(f"📝 主要意图: {analysis_result['main_intent']}")
        # print(f"🔑 搜索关键词: {analysis_result['sub_queries']}")
        # print(f"🎯 搜索策略: {analysis_result.get('search_strategy', 'N/A')}")

        # 2. 使用混合检索搜索文档
        search_results = self.hybrid_search_documents(
            query,
            k,
            context_range
        )

        if not search_results:
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

        # 3. 构建上下文内容 - 将hybrid_search返回的结果传递给AI
        context_parts = []
        for result in search_results:
            content = result["content"]
            source = result["source"]
            context_parts.append(f"【来源: {source}】\n{content}")

            # 添加上下文段落（如果存在）
            for context_item in result.get("context", []):
                context_content = context_item["content"]
                context_source = context_item["source"]
                context_parts.append(f"【相关上下文 - 来源: {context_source}】\n{context_content}")

        full_context = "\n\n".join(context_parts)

        # 4. 构建消息并调用API
        system_prompt = PROMPT_CONFIG["answer_generator"]["system_prompt"]

        messages = [{"role": "system", "content": system_prompt}]

        # 添加对话历史
        messages.extend(self.conversation.get_history())

        # 添加上下文和当前问题 - 这里将检索到的内容传递给AI
        user_message = f"基于以下检索到的文档内容回答问题：\n\n{full_context}\n\n问题：{query}"
        messages.append({"role": "user", "content": user_message})

        # 调用API生成答案
        ai_answer = self.call_deepseek_api(messages)

        # 5. 构建结果
        result = {
            "query": query,
            "analysis": analysis_result,
            "matched_sources": list(set([result["source"] for result in search_results])),
            "total_documents": len(search_results),
            "context_length": len(full_context),
            "answer": ai_answer,
            "search_results": search_results
        }

        # 6. 更新对话历史
        self.conversation.add_message("user", query)
        self.conversation.add_message("assistant", ai_answer)

        return result


def print_interactive_results(result):
    """以交互式格式打印结果"""
    print(f"\n{'=' * 80}")
    print(f"📋 问题分析结果")
    print(f"{'=' * 80}")
    print(f"🔍 用户问题: {result['query']}")
    # print(f"🎯 主要意图: {result['analysis']['main_intent']}")
    # print(f"🔑 搜索关键词: {', '.join(result['analysis']['sub_queries'])}")
    print(f"📚 找到文档: {result['total_documents']} 个")
    print(f"📖 来源文件: {', '.join(result['matched_sources'])}")
    print(f"📝 上下文长度: {result['context_length']} 字符")

    print(f"\n🤖 AI回答:")
    print(f"{'─' * 40}")
    print(result['answer'])
    print(f"{'─' * 40}")

    if 'search_results' in result and result['search_results']:
        print(f"\n📄 参考文档:")
        for i, doc in enumerate(result['search_results']):
            content_preview = doc['content'][:100] + "..." if len(doc['content']) > 100 else doc['content']
            print(f"  {i + 1}. {doc['source']}: {content_preview}")


def interactive_chat(vector_store, bm25_instance, all_splits):
    """交互式聊天界面"""
    print("\n🚀 初始化问答系统...")
    qa_system = QASystem(vector_store, bm25_instance, all_splits)

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
                qa_system.conversation.clear_history()
                print("🗑️ 对话历史已清除")
                continue
            elif not user_input:
                continue

            # 处理查询
            result = qa_system.process_query(user_input)
            print_interactive_results(result)

        except KeyboardInterrupt:
            print("\n👋 用户中断，再见!")
            break
        except Exception as e:
            print(f"❌ 处理问题时出错: {e}")