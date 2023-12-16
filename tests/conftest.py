import logging
import subprocess
import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from framework import LoginPage
from utils import android_get_desired_capabilities
from utils.utils import valid_user
from tests.utils.utils import perform_login, perform_logout


@pytest.fixture(scope='session')
def run_appium_server(logger):
    """Fixture to start the Appium server."""
    logger.info("Starting Appium server")
    process = subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(20)
    yield
    process.terminate()
    logger.info("Appium server terminated")


@pytest.fixture(scope='session')
def driver(run_appium_server, logger):
    """Fixture to provide a WebDriver instance."""
    def get_first_udid():
        """Helper function to get device's UDID."""
        result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, text=True)
        lines = result.stdout.splitlines()
        for line in lines[1:]:
            if 'device' in line and 'offline' not  in line:
                return line.split('\t')[0]
        raise RuntimeError('No devices found')
    logger.info("Initializing WebDriver")
    udid = get_first_udid()
    capabilities = android_get_desired_capabilities()
    capabilities.update(udid=udid)
    driver = webdriver.Remote('http://localhost:4723',
                              options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.quit()
    logger.info("WebDriver terminated")


@pytest.fixture(scope='class')
def login_page(driver, logger):
    """Fixture to provide a LoginPage instance."""
    time.sleep(10)
    login_page = LoginPage(driver)
    yield login_page


@pytest.fixture(scope='class')
def login_to_app(login_page, logger):
    """Fixture to perform login in the app."""
    logger.info("Performing login")
    perform_login(login_page)
    login_page.login(**valid_user)
    yield


@pytest.fixture(scope='class')
def logout(login_page, logger):
    """Fixture to perform logout from the app."""
    yield
    perform_logout(login_page)
    logger.info("Logout performed")


@pytest.fixture(scope='session')
def logger():
    """Fixture to configure and provide a logger."""
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger()
