from selenium.webdriver.common.by import By

from hw_13.utilities.web_ui.locator import Locator


class BlogPageLocators:
    def __init__(self):
        self.__another_menu = Locator(method=By.XPATH, locator='//li[@class="other desktop-item"]/a')
        self.__blog = Locator(method=By.XPATH, locator='//li/div/div[3]/a')
        self.__blog_title = Locator(method=By.XPATH, locator='//div[@class="page-title category-title"]')
        self.__post_list = Locator(method=By.XPATH, locator='//*[@id="post-list"]')
        self.__side_bar = Locator(method=By.XPATH, locator='//div[@class="col-left sidebar grid12-3 grid-col2-sidebar no-gutter"]')

    @property
    def another_menu_item(self):
        return self.__another_menu.get_locator()

    @property
    def blog(self):
        return self.__blog.get_locator()

    @property
    def blog_title(self):
        return self.__blog_title.get_locator()

    @property
    def post_list(self):
        return self.__post_list.get_locator()

    @property
    def side_bar(self):
        return self.__side_bar.get_locator()
