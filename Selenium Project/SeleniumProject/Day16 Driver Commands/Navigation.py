import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="127.0.6533.89").install()))
driver.get("https://www.facebook.com")
driver.get("https://www.amazon.com")
driver.back()
driver.forward()
driver.refresh()
time.sleep(2)
driver.quit()