import json
import pytest
from hw_13.CONSTANTS import ROOT_DIR
from hw_13.data_classes.post import Post
from hw_13.data_classes.user import User
from hw_13.page_objects.blog_page.blog_page import BlogPage
from hw_13.page_objects.login_page.login_page import LoginLink
from hw_13.utilities.configuration import Configuration
from hw_13.utilities.driver_factory import DriverFactory


def pytest_configure(config):
    """
    This function register an additional marker
    :param config:
    """
    config.addinivalue_line(
        "markers", 'regression: for regression'
    )
    config.addinivalue_line(
        "markers", 'smoke: for smoke'
    )


@pytest.fixture(scope="session")
def env():
    """
    This fixture gives access to configuraton.json
    :return: dict
    """
    with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)
    configs = Configuration(**json_to_dict)
    return configs


@pytest.fixture
def create_driver(env):
    """
    This fixture creates friver
    :param env: base_url
    :return: driver
    """
    driver = DriverFactory.create_driver(env.browser_id)
    driver.maximize_window()
    driver.get(env.base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_link(create_driver):
    """
    This fixture openes login page
    :param create_driver:
    :return: LoginLink
    """
    return LoginLink(create_driver)


@pytest.fixture()
def open_blog_page(create_driver):
    """
    This fixture openes blog page
    :param create_driver:
    :return: BlogPage
    """
    return BlogPage(create_driver)


@pytest.fixture()
def create_person():
    return User()


@pytest.fixture()
def create_post():
    return Post()
