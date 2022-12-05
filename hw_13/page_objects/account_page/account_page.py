from hw_13.page_objects.account_page.account_page_locators import AccountPageLocators
from hw_13.utilities.web_ui.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(driver)
        self.__locators = AccountPageLocators()

    def is_contact_edit_visible(self) -> 'bool':
        return self._is_visible(self.__locators.edit_contact_info)

    def is_required_password_visible(self) -> 'bool':
        return self._is_visible(self.__locators.required_password)

    def is_required_email_visible(self) -> 'bool':
        return self._is_visible(self.__locators.required_email)

    def is_welcome_message_visible(self) -> 'bool':
        return self._is_visible(self.__locators.welcome_message)

    def click_edit(self):
        self._click(self.__locators.edit_contact_info)
        return self

    def click_edit_address(self):
        self._click(self.__locators.address_edit)
        return self

    def edit_account(self):
        self.click_edit()
        return AccountPage(self.__driver)

    def is_edit_account_title_visible(self) -> 'bool':
        return self._is_visible(self.__locators.edit_account_title)

    def edit_address(self):
        self.click_edit_address()
        return AccountPage(self.__driver)

    def is_edit_address_link_visible(self) -> 'bool':
        return self._is_visible(self.__locators.address_edit)

    def is_edit_address_title_visible(self) -> 'bool':
        return self._is_visible(self.__locators.address_edit_title)
