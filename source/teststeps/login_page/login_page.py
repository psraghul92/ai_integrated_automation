import pytest
from resources.test_data import LOGIN_CREDENTIALS
from source.utilities.config_utilities import load_yaml_file

login_credentials = load_yaml_file(LOGIN_CREDENTIALS)

LOGIN_SUCCESS = (
    'Important: Iam UI Automation tester validating the tasks '
    f'Open website {pytest.base_url} '
    f'Enter username {login_credentials['valid_username']} '
    f'Enter password {login_credentials['valid_password']} '
    'Click on login button '
    'Validate if Cart icon is displayed '
)

LOGIN_FAILURE = (
    'Important: Iam UI Automation tester validating the tasks '
    f'Open website {pytest.base_url} '
    f'Enter username {login_credentials['invalid_username']} '
    f'Enter password {login_credentials['invalid_password']} '
    'Click on login button '
    'Validate if error message is displayed '
    'Get the error message displayed '
)
