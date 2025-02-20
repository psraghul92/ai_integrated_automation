import os
import pytest

from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI


async def run_test(test_case= None, report_file_name = None, output_model_object = None):
    llm = get_llm_object()
    controller_object = Controller(output_model=output_model_object)
    agent = Agent(test_case, llm, use_vision=False,controller=controller_object)
    history = await agent.run()
    history.save_to_file(f"report/{report_file_name}.txt")
    test_result = history.final_result()
    actual_result = output_model_object.model_validate_json(test_result)
    return actual_result


def get_llm_object():
    llm = None
    if pytest.llm_model == "gemini-2.0-flash-exp":
        api_key = os.environ['GEMINI_API_KEY']
        llm = ChatGoogleGenerativeAI(model= pytest.llm_model, api_key=api_key)
    return llm