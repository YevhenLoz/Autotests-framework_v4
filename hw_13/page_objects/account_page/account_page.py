from hw_13.page_objects.account_page.account_page_locators import AccountPageLocators
from hw_13.utilities.web_ui.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(driver)
        self.__locators = AccountPageLocators()

    def contact_edit_visible(self):
        return self._is_visible(self.__locators.edit_contact_info)

    def required_password_visible(self):
        return self._is_visible(self.__locators.required_password)

    def required_email_visible(self):
        return self._is_visible(self.__locators.required_email)

    def welcome_message_visible(self):
        return self._is_visible(self.__locators.welcome_message)

    def click_edit(self):
        return self._click(self.__locators.edit_contact_info)

    def click_edit_address(self):
        return self._click(self.__locators.address_edit)

    def edit_account(self):
        self.click_edit()
        return AccountPage(self.__driver)

    def edit_account_title_visible(self):
        return self._is_visible(self.__locators.edit_account_title)

    def edit_address(self):
        self.click_edit_address()
        return AccountPage(self.__driver)

    def edit_address_link(self):
        return self._is_visible(self.__locators.address_edit)

    def edit_address_title_visible(self):
        return self._is_visible(self.__locators.address_edit_title)
