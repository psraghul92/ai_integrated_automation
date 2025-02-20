import pytest
import allure
from assertpy import soft_assertions, assert_that

from source.ai_agent.ai_agent import run_test
from source.teststeps.full_transactions.full_transaction import FULL_TRANSACTION
from source.validations.full_transaction import ValidateSuccessfulTransaction


@allure.parent_suite("SAUCE LABS DEMO")
@allure.sub_suite("FULL TRANSACTION TESTS")
class TestFullTransaction:

    @pytest.mark.asyncio
    async def test_successful_transaction(self, request):
        with allure.step(FULL_TRANSACTION):
            actual_result = await run_test(test_case=FULL_TRANSACTION, report_file_name=request.node.name,
                                           output_model_object=ValidateSuccessfulTransaction)
            print(actual_result)
        with allure.step("Validate if transaction is successful"):
            with soft_assertions():
                assert_that(actual_result.cart_item_count, description='Expected cart item count:1 '
                                                                       f'Actual:{actual_result.cart_item_count}').is_equal_to(
                    1)
                assert_that(actual_result.total_price, description='Expected total price:$32.39 '
                                                                   f'Actual: {actual_result.total_price}').is_equal_to(
                    '$32.39')
                assert_that(actual_result.checkout_complete_message, description='Expected: Thank you for your order! '
                                                                                 f'Actual:{actual_result.checkout_complete_message}').is_equal_to(
                    'Thank you for your order!')
