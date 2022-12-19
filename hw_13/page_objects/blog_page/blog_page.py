from hw_13.page_objects.blog_page.blog_page_locators import BlogPageLocators
from hw_13.utilities.web_ui.base_page import BasePage
import allure


class BlogPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(driver)
        self.__locators = BlogPageLocators()

    @allure.step
    def click_another_menu(self):
        self._click(self.__locators.another_menu_item)
        return self

    @allure.step
    def click_blog(self):
        self._click(self.__locators.blog)
        return self

    @allure.step
    def is_blog_title_visible(self) -> 'bool':
        return self._is_visible(self.__locators.blog_title)

    @allure.step
    def go_to_blog(self):
        self.click_another_menu().click_blog()
        return BlogPage(self.__driver)

    @allure.step
    def is_post_list_visible(self) -> 'bool':
        return self._is_visible(self.__locators.post_list)

    @allure.step
    def is_side_bar_visible(self) -> 'bool':
        return self._is_visible(self.__locators.side_bar)
