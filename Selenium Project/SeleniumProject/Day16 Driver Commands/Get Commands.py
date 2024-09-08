from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(service=Service(ChromeDriverManager(driver_version='127.0.6533.73').install()))
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()


