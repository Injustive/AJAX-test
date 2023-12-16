import pytest
from utils.utils import (generate_random as random_chars,
                                              generate_random_email as random_email,
                                              valid_user)
from utils import xpath_utils


class TestLogin:
    @pytest.mark.parametrize('login, password, expected', [
        ("", "", False),
        ("", random_chars(), False),
        (random_chars(), "", False),
        (random_chars(), random_chars(), True),
    ])
    def test_is_login_button_active(self, login_start_page, back_to_login, logger, login, password, expected):
        """Tests the active state of the login button with various login/password combinations."""
        logger.info(f"Testing login button activation: login='{login}', password='{password}'")
        login_start_page.send_data_to_login_fields(login, password)
        is_button_active = login_start_page.login_btn.is_enabled()
        logger.info(f"Button active state. Actual: {is_button_active}. Expected: {expected}")
        assert is_button_active == expected, "Login button active state did not match expected"

    @pytest.mark.parametrize('login, password, expected', [
        (random_email(), random_chars(), 'Wrong login or password'),
        (random_chars(), random_chars(), 'Invalid email format')
    ])
    def test_email_format_correctness(self, driver, login_start_page, back_to_login, logger, login, password, expected):
        """Tests the UI response to the correctness of the email format."""
        logger.info(f"Testing email format correctness: login='{login}', password='{password}'")
        login_start_page.login(login, password)
        snackbar = login_start_page.presence_of_element_located(xpath_utils.INVALID_DATA_SNACKBAR)
        logger.info(f"Snackbar text. Actual: '{snackbar.text}', Expected: '{expected}'")
        assert snackbar.text == expected, f"Snackbar text '{snackbar.text}' does not match expected '{expected}'"

    def test_login_positive(self, driver, login_into_app, logout, logger):
        """Checks for successful login with valid user credentials."""
        logger.info("Testing positive login scenario with correct user data")
        menu_drawer = login_into_app.presence_of_element_located(xpath_utils.MENU_DRAWER_XPATH)
        logger.info(f"Menu drawer found. Actual: {menu_drawer.is_displayed()}. Expected: True")
        assert menu_drawer, "Menu drawer was not found, login might have failed"

    @pytest.mark.parametrize('login, password', [
        (valid_user['login'], random_chars()),
        (random_chars(), valid_user['password']),
        (random_chars(), random_chars())
    ])
    def test_login_negative(self, driver, login_start_page, back_to_login, logger, login, password):
        """Tests negative login scenarios with incorrect user credentials."""
        logger.info(f"Testing negative login scenario with login: '{login}', password: '{password}'")
        login_start_page.login(login, password)
        snackbar = login_start_page.presence_of_element_located(xpath_utils.INVALID_DATA_SNACKBAR)
        logger.info(f"Snackbar indicating bad data. Actual: {snackbar.is_displayed()}, Expected: True")
        assert snackbar, "Snackbar indicating bad data was not found. Maybe unexpected login success"
