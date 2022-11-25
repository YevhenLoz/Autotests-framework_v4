from selenium.webdriver.common.by import By

from hw_13.utilities.web_ui.locator import Locator


class ForgotPasswordPageLocators:
    def __init__(self):
        self.__required_email = Locator(method=By.XPATH, locator='//input[@id="email_address"]')
        self.__confirm_button = Locator(method=By.XPATH, locator='//button[@class="button"]')
        self.__forgot_password_page_title = Locator(method=By.XPATH, locator='//div[@class="page-title"]/h1')
        self.__success_message = Locator(method=By.XPATH, locator='//li[@class="success-msg"]')
        self.__validation_message = Locator(method=By.XPATH, locator='//div[@id="advice-required-entry-email_address"]')
        self.__validation_email = Locator(method=By.XPATH, locator='//div[@id="advice-validate-email-email_address"]')

    @property
    def required_email(self):
        return self.__required_email.get_locator()

    @property
    def confirm_button(self):
        return self.__confirm_button.get_locator()

    @property
    def forgot_password_page_title(self):
        return self.__forgot_password_page_title.get_locator()

    @property
    def success_message(self):
        return self.__success_message.get_locator()

    @property
    def validation_message(self):
        return self.__validation_message.get_locator()

    @property
    def validation_email(self):
        return self.__validation_email.get_locator()
