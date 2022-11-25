from hw_13.page_objects.forgotpassword_page.forgotpassword_page_locators import ForgotPasswordPageLocators

from hw_13.utilities.web_ui.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(driver)
        self.__locators = ForgotPasswordPageLocators()

    def set_forgot_password_email(self, email):
        self._send_keys(self.__locators.required_email, email)
        return self

    def click_confirm(self):
        self._click(self.__locators.confirm_button)
        return self

    def forgot_password_page_title_visible(self):
        return self._is_visible(self.__locators.forgot_password_page_title)

    def forgot_password_confirm(self, email2):
        self.set_forgot_password_email(email2).click_confirm()
        return ForgotPasswordPage(self.__driver)

    def success_message_visible(self):
        return self._is_visible(self.__locators.success_message)

    def forgot_password_confirm_empty_email(self):
        self.click_confirm()
        return ForgotPasswordPage(self.__driver)

    def validation_message_visible(self):
        return self._is_visible(self.__locators.validation_message)

    def forgot_pass_confirm_invalid_email(self, invalid_email):
        self.set_forgot_password_email(invalid_email).click_confirm()
        return ForgotPasswordPage(self.__driver)

    def validation_email_visible(self):
        return self._is_visible(self.__locators.validation_email)
