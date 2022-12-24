from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id: int, is_headless=True):
        if int(driver_id) == DriverFactory.CHROME:
            chrome_options = Options()
            if is_headless:
                chrome_options.addArguments("--window-size=1920,1080") 
                chrome_options.addArguments("--disable-gpu") 
                chrome_options.addArguments("-- disable-extensions") 
                chrome_options.setExperimentalOption("useAutomationExtension", false) 
                chrome_options.addArguments("--proxy-server='direct://'") 
                chrome_options.addArguments("--proxy-bypass-list=*") 
                chrome_options.addArguments("--start-maximized")
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--no-sandbox")
            driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        elif int(driver_id) == DriverFactory.FIREFOX:
            driver = Firefox(service=Service(GeckoDriverManager().install()))
        elif int(driver_id) == DriverFactory.EDGE:
            driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver
