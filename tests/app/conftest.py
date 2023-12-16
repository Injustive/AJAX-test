import pytest
from framework import App


@pytest.fixture(scope='class')
def app(driver, login_to_app, logger):
    """Initializes the App class and logs into the application."""
    logger.info("Initializing the App class and logging into the application.")
    app = App(driver)
    yield app


@pytest.fixture
def sidebar(driver, app, logger):
    """Opens the sidebar menu and closes it after the test."""
    logger.info("Opening the sidebar menu.")
    app.click_element(app.menu_drawer)
    yield app
    logger.info("Closing the sidebar menu.")
    sidebar = app.sidebar
    element_location = sidebar.location
    element_size = sidebar.size
    start_x = element_location['x'] + element_size['width'] // 2
    start_y = element_location['y'] + element_size['height'] // 2
    end_x = element_location['x']
    end_y = start_y
    driver.swipe(start_x, start_y, end_x, end_y, duration=100)
