from .page import Page
from utils import xpath_utils


class LoginPage(Page):
    def send_data_to_login_fields(self, login, password):
        """Fill in the login and password fields with provided credentials."""
        self.login_field.send_keys(login)
        self.password_field.send_keys(password)

    def clean_login_fields(self):
        """Clear the login and password fields."""
        self.login_field.clear()
        self.password_field.clear()

    def login(self, login, password):
        """Log into the application using specified login and password."""
        self.send_data_to_login_fields(login, password)
        self.click_element(self.login_btn)

    @property
    def login_field(self):
        """Return the WebElement of the login field."""
        return self.presence_of_element_located(xpath_utils.LOGIN_EMAIL_XPATH)

    @property
    def password_field(self):
        """Return the WebElement of the password field."""
        return self.presence_of_element_located(xpath_utils.LOGIN_PASSWORD_XPATH)

    @property
    def login_btn(self):
        """Return the WebElement of the login button."""
        return self.find_element(xpath_utils.LOGIN_BUTTON_XPATH)

    @property
    def main_login_btn(self):
        """Return the WebElement of the main login button."""
        return self.find_element(xpath_utils.MAIN_LOGIN_BUTTON_XPATH)
