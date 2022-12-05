from selenium.webdriver.common.by import By

from hw_13.utilities.web_ui.locator import Locator


class AccountPageLocators:
    def __init__(self):
        self.__edit_contact_info = Locator(method=By.XPATH, locator='//div[@class="box contact-info"]/div/a')
        self.__required_password = Locator(method=By.XPATH, locator='//div[@id="advice-required-entry-pass"]')
        self.__required_email = Locator(method=By.XPATH, locator='// div[ @ id = "advice-required-entry-email"]')
        self.__welcome_message = Locator(method=By.XPATH, locator='//p[@class="hello"]/strong')
        self.__edit_account_title = Locator(method=By.XPATH, locator='//div[@class="my-account"]/div/h1')
        self.__address_edit = Locator(method=By.XPATH, locator='//div/a[contains(@href, "address")]')
        self.__address_edit_title = Locator(method=By.XPATH, locator='//div[@class="page-title"]/h1')

    @property
    def edit_contact_info(self):
        return self.__edit_contact_info.get_locator()

    @property
    def required_password(self):
        return self.__required_password.get_locator()

    @property
    def required_email(self):
        return self.__required_email.get_locator()

    @property
    def welcome_message(self):
        return self.__welcome_message.get_locator()

    @property
    def edit_account_title(self):
        return self.__edit_account_title.get_locator()

    @property
    def address_edit(self):
        return self.__address_edit.get_locator()

    @property
    def address_edit_title(self):
        return self.__address_edit_title.get_locator()
