import logging

from arklex.utils.model_config import MODEL
from arklex.utils.model_provider_config import PROVIDER_MAP
from arklex.env.prompts import load_prompts
from arklex.utils.graph_state import MessageState

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools import TavilySearchResults


logger = logging.getLogger(__name__)


class SearchEngine():
    def __init__(self):
        self.llm = PROVIDER_MAP.get(MODEL['llm_provider'], ChatOpenAI)(
            model=MODEL["model_type_or_path"], timeout=30000
        )
        self.search_tool = TavilySearchResults(
            max_results=5,
            search_depth="advanced",
            include_answer=True,
            include_raw_content=True,
            include_images=False,
        )

    #def process_search_result(self, search_results):
    #    search_text = ""
    #   for res in search_results:
    #       search_text += f"Source: {res['url']} \n"
    #       search_text += f"Content: {res['content']} \n\n"
    #   return search_text
    def process_search_result(self, search_results):
        import json

        search_text = ""

        # Debug print (可移除)
        logger.debug(f"[SEARCH] Raw results: {type(search_results)} - {search_results}")

        # 如果是字串，嘗試轉成 JSON
        if isinstance(search_results, str):
            try:
                search_results = json.loads(search_results)
            except Exception as e:
                logger.warning(f"Failed to parse search_results as JSON: {e}")
                return "⚠️ Search results could not be processed."

        # 確保是 list，才可以迭代
        if isinstance(search_results, list):
            for res in search_results:
                if isinstance(res, dict):
                    url = res.get("url", "No URL")
                    content = res.get("content", "No content")
                    search_text += f"Source: {url}\nContent: {content}\n\n"
                else:
                    search_text += f"⚠️ Unexpected format: {res}\n"
        else:
            search_text = f"⚠️ Unexpected search_results type: {type(search_results)}"

        return search_text


    def search(self, state: MessageState):
        prompts = load_prompts(state["bot_config"])
        contextualize_q_prompt = PromptTemplate.from_template(
            prompts["retrieve_contextualize_q_prompt"]
        )
        ret_input_chain = contextualize_q_prompt | self.llm | StrOutputParser()
        ret_input = ret_input_chain.invoke({"chat_history": state["user_message"].history})
        logger.info(f"Reformulated input for search engine: {ret_input}")
        search_results = self.search_tool.invoke({"query": ret_input})
        state["message_flow"] = self.process_search_result(search_results)
        return state
