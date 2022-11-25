from hw_13.page_objects.blog_page.blog_page_locators import BlogPageLocators
from hw_13.utilities.web_ui.base_page import BasePage


class BlogPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(driver)
        self.__locators = BlogPageLocators()

    def click_another_menu(self):
        self._click(self.__locators.another_menu_item)
        return self

    def click_blog(self):
        self._click(self.__locators.blog)
        return self

    def blog_title_is_visible(self):
        return self._is_visible(self.__locators.blog_title)

    def go_to_blog(self):
        self.click_another_menu().click_blog()
        return BlogPage(self.__driver)

    def post_list_is_visible(self):
        return self._is_visible(self.__locators.post_list)

    def side_bar_is_visible(self):
        return self._is_visible(self.__locators.side_bar)