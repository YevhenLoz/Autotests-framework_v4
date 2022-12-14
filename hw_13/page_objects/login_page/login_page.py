from hw_13.page_objects.account_page.account_page import AccountPage
from hw_13.page_objects.create_account_page.create_account_page import CreateAccount
from hw_13.page_objects.forgotpassword_page.forgotpassword_page import ForgotPasswordPage
from hw_13.page_objects.login_page.login_page_locators import LoginPageLocators
from hw_13.utilities.web_ui.base_page import BasePage
import allure


class LoginLink(BasePage):
    def __init__(self, driver):
        self.__driver = driver
        super().__init__(driver)
        self.__locators = LoginPageLocators()

    @allure.step
    def click_login_link(self):
        self._click(self.__locators.login_link)
        return self

    @allure.step
    def set_email(self, email):
        self._send_keys(self.__locators.email_input, email)
        return self

    @allure.step
    def set_password(self, password):
        self._send_keys(self.__locators.password_input, password)
        return self

    @allure.step
    def click_login(self):
        self._click(self.__locators.login_button)
        return self

    @allure.step
    def click_logout(self):
        self._click(self.__locators.logout_link)
        return self

    @allure.step
    def click_create_account(self):
        self._click(self.__locators.create_account_button)
        return self

    @allure.step
    def open_cabinet(self):
        self._click(self.__locators.cabinet)
        return self

    @allure.step
    def is_logout_link_visible(self) -> 'bool':
        return self._is_visible(self.__locators.logout_link)

    @allure.step
    def is_forgot_password_present(self) -> 'bool':
        return self._is_visible(self.__locators.forgot_password)

    @allure.step
    def click_forgot_password(self):
        self._click(self.__locators.forgot_password)
        return self

    @allure.step
    def is_logout_link_invisible(self) -> 'bool':
        return self._is_invisible(self.__locators.logout_link)

    @allure.step
    def login(self, email, password):
        self.click_login_link().set_email(email).set_password(password).click_login().open_cabinet()
        return LoginLink(self.__driver)

    @allure.step
    def go_to_login(self):
        self.click_login_link()
        return LoginLink(self.__driver)

    @allure.step
    def logout(self, email, password):
        self.click_login_link().set_email(email).set_password(password).click_login().open_cabinet().click_logout()
        return LoginLink(self.__driver)

    @allure.step
    def account(self, email, password):
        self.click_login_link().set_email(email).set_password(password).click_login()
        return AccountPage(self.__driver)

    @allure.step
    def login_with_empty_password(self, email):
        self.click_login_link().set_email(email).click_login()
        return AccountPage(self.__driver)

    @allure.step
    def login_with_empty_email(self, password):
        self.click_login_link().set_password(password).click_login()
        return AccountPage(self.__driver)

    @allure.step
    def go_to_create_account(self):
        self.click_login_link().click_create_account()
        return CreateAccount(self.__driver)

    @allure.step
    def go_to_forgot_password(self):
        self.click_login_link().click_forgot_password()
        return ForgotPasswordPage(self.__driver)

    @allure.step
    def login_without_creds(self):
        self.click_login_link().click_login()
        return AccountPage(self.__driver)
