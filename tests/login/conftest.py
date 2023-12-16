import pytest
from utils import xpath_utils
from utils.utils import valid_user
from tests.utils.utils import perform_login, perform_logout


@pytest.fixture
def login_start_page(login_page, logger):
    """Makes a transition to the login page. Performs necessary login setup"""
    logger.info('Go to main login page')
    perform_login(login_page)
    yield login_page


@pytest.fixture
def login_into_app(login_start_page, logger):
    """Login into the app"""
    logger.info('Login into the app')
    login_start_page.login(**valid_user)
    yield login_start_page


@pytest.fixture()
def logout(login_page, logger):
    """Logs out from the app page post-test execution."""
    logger.info('Logout from the app page')
    yield
    perform_logout(login_page)


@pytest.fixture
def back_to_login(login_page, logger):
    """Makes a transition to the main login page"""
    yield
    logger.info('Back to the main login page')
    login_page.click_element(login_page.find_element(xpath_utils.BACK_ARROW_XPATH))
