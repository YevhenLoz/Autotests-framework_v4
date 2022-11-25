from selenium.webdriver.common.by import By

from hw_13.utilities.web_ui.locator import Locator


class LoginPageLocators:
    def __init__(self):
        self.__login_link = Locator(method=By.XPATH, locator='//ul//*[@id="mini-account-wrapper-regular-slip"]/a')
        self.__email_input = Locator(method=By.XPATH, locator='//input[@type ="email"]')
        self.__password_input = Locator(method=By.XPATH, locator='//input[@id ="pass"]')
        self.__login_button = Locator(method=By.XPATH, locator='//button[@type="submit" and @id ="send2"] ')
        self.___cabinet = Locator(method=By.XPATH, locator='//ul//div[@id="mini-account"]')
        self.__logout_link = Locator(method=By.XPATH, locator='//ul//div[@id="header-account"]/ul/li[@class=" last"]/a')
        self.__forgot_password_link = Locator(method=By.XPATH, locator='//div[@class="buttons-set"]/a')
        self.__create_account_button = Locator(method=By.XPATH, locator='//div[@class="new-users grid12-6"]//button')

    @property
    def login_link(self):
        return self.__login_link.get_locator()

    @property
    def email_input(self):
        return self.__email_input.get_locator()

    @property
    def password_input(self):
        return self.__password_input.get_locator()

    @property
    def login_button(self):
        return self.__login_button.get_locator()

    @property
    def cabinet(self):
        return self.___cabinet.get_locator()

    @property
    def logout_link(self):
        return self.__logout_link.get_locator()

    @property
    def forgot_password(self):
        return self.__forgot_password_link.get_locator()

    @property
    def create_account_button(self):
        return self.__create_account_button.get_locator()
