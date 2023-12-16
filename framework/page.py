from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        """Initializes the page with a given web driver."""
        self.driver = driver

    def find_element(self, value, by=AppiumBy.XPATH):
        """Locate an element on the page using a specified selector."""
        return self.driver.find_element(value=value, by=by)

    @staticmethod
    def click_element(element):
        """Click on the specified web element."""
        element.click()

    def presence_of_element_located(self, xpath):
        """Wait until an element is present on the page, located by XPath."""
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
