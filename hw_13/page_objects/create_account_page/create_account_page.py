from hw_13.page_objects.create_account_page.create_account_page_locators import CreateAccountLocators
from hw_13.utilities.web_ui.base_page import BasePage


class CreateAccount(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(driver)
        self.__locators = CreateAccountLocators()

    def is_create_account_title_visible(self) -> 'bool':
        return self._is_visible(self.__locators.account_create_title)

    def click_back_to_login(self):
        self._click(self.__locators.back_to_login)
        return self

    def is_login_page_title_visible(self) -> 'bool':
        return self._is_visible(self.__locators.login_page_title)

    def go_back_to_login(self):
        self.click_back_to_login()
        return CreateAccount(self.__driver)

    def click_submit_button(self):
        self._click(self.__locators.submit_button)
        return self

    def is_name_required_visible(self) -> 'bool':
        return self._is_visible(self.__locators.validation_name)

    def submit_without_name(self):
        self.click_submit_button()
        return CreateAccount(self.__driver)

    def is_name_field_visible(self) -> 'bool':
        return self._is_visible(self.__locators.input_name())
