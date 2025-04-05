
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.edge.service import Service as EdgeDriverService

from selenium.webdriver.firefox.options import Options

from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.firefox import GeckoDriverManager



class TestClass:
    def test_login_from_chrome(self):
        # Set up Chrome WebDriver using webdriver-manager

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.arrow.com/")

        # Perform actions or assertions here

        print(f"Chrome Browser Title: {self.driver.title}")

        self.driver.quit()

    def test_login_from_edge(self):
        # Set up Edge WebDriver using webdriver-manager

        self.driver = webdriver.Edge(service=EdgeDriverService(EdgeChromiumDriverManager().install()))
        self.driver.get("https://www.arrow.com/")

        # Perform actions or assertions here

        print(f"Edge Browser Title: {self.driver.title}")

        self.driver.quit()

    def test_login_from_firefox(self):
        # Set up Firefox WebDriver using webdriver-manager

        options = Options()
        # Provide Firefox binary location (if needed)
        options.binary_location = r"C:\Users\148350\AppData\Local\Mozilla Firefox\firefox.exe"
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.get("https://www.arrow.com/")

        # Perform actions or assertions here

        print(f"Firefox Browser Title: {self.driver.title}")

        self.driver.quit()

