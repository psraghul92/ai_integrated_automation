import pytest
from resources.test_data import LOGIN_CREDENTIALS
from source.utilities.config_utilities import load_yaml_file

login_credentials = load_yaml_file(LOGIN_CREDENTIALS)

FULL_TRANSACTION = (
    'Important: Iam UI Automation tester validating the a full transaction'
    f'Open website {pytest.base_url} '
    f'Enter username {login_credentials['valid_username']} '
    f'Enter password {login_credentials['valid_password']} '
    'Click on login button '
    'Add Sauce Labs Backpack to cart '
    'Click on cart icon '
    'After landing in cart page,click checkout'
    f'Enter the first name as {login_credentials['valid_username']}'
    f'Enter the last name as test'
    f'Enter the Zip/postal code as 12345'
    'click on continue button'
    'click on finish button'
)

