"""from requests import options
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager(version="130.0.0").install()))
driver.get("https://ww.arrow.com")"""
from requests import options
#exutablepath ="""C:\Users\148350\AppData\Local\Mozilla Firefox"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
ops = Options()
ops.binary_location = r'C:\Users\148350\AppData\Local\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=ops)


driver.get("https://www.arrow.com")
