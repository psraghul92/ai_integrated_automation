import pytest
import os
import shutil
import allure
from source.utilities.config_utilities import get_base_url, get_llm_model

AGENT_HISTORY_FILE = 'agent_history.gif'


def pytest_configure():
    pytest.base_url = get_base_url()
    pytest.llm_model = get_llm_model()
    if os.path.exists('report'):
        shutil.rmtree('report')
    if os.path.isfile(AGENT_HISTORY_FILE):
        os.remove(AGENT_HISTORY_FILE)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.failed or report.passed:
        if os.path.isfile(f'report/{item.name}.txt') and os.path.isfile(AGENT_HISTORY_FILE):
            allure.attach.file(f"report/{item.name}.txt", name=item.name, attachment_type=allure.attachment_type.TEXT,
                           extension='txt')
            allure.attach.file(AGENT_HISTORY_FILE, name=f"{item.name}_history", attachment_type=allure.attachment_type.GIF,
                           extension='gif')
            os.remove('agent_history.gif')
