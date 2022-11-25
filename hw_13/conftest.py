import pytest

from hw_13.page_objects.blog_page.blog_page import BlogPage
from hw_13.page_objects.login_page.login_page import LoginLink
from hw_13.utilities.driver_factory import DriverFactory
from hw_13.utilities.read_configs import ReadConfig


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        "markers", 'regression: for regression'
    )
    config.addinivalue_line(
        "markers", 'smoke: for smoke'
    )


@pytest.fixture()
def create_driver():
    driver_chrome = DriverFactory.create_driver(ReadConfig.get_browser_id())
    driver_chrome.maximize_window()
    driver_chrome.get(ReadConfig.get_base_url())
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture()
def open_login_link(create_driver):
    return LoginLink(create_driver)


@pytest.fixture()
def open_blog_page(create_driver):
    return BlogPage(create_driver)
