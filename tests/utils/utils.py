from utils import xpath_utils


def perform_login(login_page):
    """Helper function to prepare login page"""
    main_btn = login_page.presence_of_element_located(xpath_utils.MAIN_LOGIN_BUTTON_XPATH)
    login_page.click_element(main_btn)
    login_page.clean_login_fields()


def perform_logout(login_page):
    """Helper function for logout"""
    login_page.click_element(login_page.find_element(xpath_utils.MENU_DRAWER_XPATH))
    login_page.click_element(login_page.find_element(xpath_utils.APP_SETTINGS_XPATH))
    login_page.click_element(login_page.find_element(xpath_utils.LOGOUT_XPATH))
