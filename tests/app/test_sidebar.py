import pytest
from utils import xpath_utils


class TestSidebar:
    @pytest.mark.parametrize('sidebar_item, item_name', xpath_utils.SIDEBAR_ELEMS_XPATHS)
    def test_sidebar_navigation(self, app, sidebar, logout, logger, sidebar_item, item_name):
        """Tests each sidebar item to ensure they are displayed properly in the UI."""
        logger.info(f"Testing visibility of sidebar item: {item_name}")
        item = app.find_element(sidebar_item)
        logger.info(f"Visibility of sidebar item {item_name}. Actual: {item.is_displayed()}. Expected: {True}")
        assert item.is_displayed()
