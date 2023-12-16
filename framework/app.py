from .page import Page
from utils import xpath_utils


class App(Page):
    @property
    def menu_drawer(self):
        """Return the WebElement of the menu drawer."""
        return self.presence_of_element_located(xpath_utils.MENU_DRAWER_XPATH)

    @property
    def sidebar(self):
        """Return the WebElement of the sidebar."""
        return self.find_element(xpath_utils.SIDEBAR_XPATH)
