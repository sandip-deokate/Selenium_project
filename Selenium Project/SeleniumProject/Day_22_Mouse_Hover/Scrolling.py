import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.arrow.com/")
driver.maximize_window()
# Scroll down page through pixel
"""driver.execute_script("window.scrollBy(0,3000)")
value= driver.execute_script("return window.pageYOffset;")
print(value)"""

#Scroll down till element is visible
ele = driver.find_element(By.XPATH," //a[normalize-space()='Our featured stories']")
#ele = driver.find_element(By.XPATH,"/html//main[@id='main-content']/section[7]//a[@href='https://careers.arrow.com/us/en']")
driver.execute_script("arguments[0].scrollIntoView();",ele)

time.sleep(5)
driver.execute_script("arguments[0].click();", ele)


# Scroll down till down

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(10)