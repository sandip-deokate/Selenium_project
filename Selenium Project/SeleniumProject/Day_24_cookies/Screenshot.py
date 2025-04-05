from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def ChromeSetUp():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    #from selenium.webdriver.chrome.options import Options
    ops = webdriver.ChromeOptions()
    #ops.add_experimental_option()
    ops.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="").install()),options=ops)

    return driver

driver= ChromeSetUp()
driver.get("https:uat.arrow.com")
#Screenshot
#driver.save_screenshot("C:\\A11ty\\sandip\\homepage.png")

#Capture coockies from browser
cookie = driver.get_cookies()
print("size", len(cookie))
"""for c in cookie:
    print(c.get('name')) # specific attribute"""
# Add cookies
driver.add_cookie({"name":"MyCookie", "value":"123456"})
cookie1 = driver.get_cookies()
print(cookie1)
driver.delete_cookie("MyCookie")
cookie2= driver.get_cookies()
print(cookie2)







