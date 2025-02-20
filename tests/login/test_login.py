import pytest
import allure
from assertpy import soft_assertions, assert_that

from source.teststeps.login_page.login_page import LOGIN_SUCCESS, LOGIN_FAILURE
from source.ai_agent.ai_agent import run_test
from source.validations.login_page import ValidateLoginSuccessful, ValidateLoginFailure


@allure.parent_suite("SAUCE LABS DEMO")
@allure.sub_suite("LOGIN TESTS")
class TestLogin:

    @pytest.mark.asyncio
    async def test_login_successful(self, request):
        with allure.step(LOGIN_SUCCESS):
            actual_result = await run_test(test_case=LOGIN_SUCCESS, report_file_name=request.node.name,
                                           output_model_object=ValidateLoginSuccessful)
        with allure.step("Validate if login is successful"):
            assert_that(actual_result.chart_icon_displayed, description='Login was not successful').is_equal_to(True)

    @pytest.mark.asyncio
    async def test_login_failure(self, request):
        with allure.step(LOGIN_FAILURE):
            actual_result = await run_test(test_case=LOGIN_FAILURE, report_file_name=request.node.name,
                                           output_model_object=ValidateLoginFailure)
        with allure.step("Validate if login is not successful and error is thrown"):
            with soft_assertions():
                assert_that(actual_result.error_message_displayed,
                            description='Error message was not displayed').is_equal_to(True)
                assert_that(actual_result.error_message,
                            description='Error message displayed is not as expected').is_equal_to(
                    'Epic sadface: Username and password do not match any user in this service')
