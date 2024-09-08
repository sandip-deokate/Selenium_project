import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="").install()))

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

#Approch1
"""windowId=driver.current_window_handle
#print(windowId)
driver.find_element(By.XPATH,"//a[@target='_blank']/button").click()
time.sleep(2)

windowIds = driver.window_handles
print(windowIds[1])
driver.switch_to.window(windowIds[1])
driver.find_element(By.XPATH,"//a[@id='navbarDropdown']").click()
time.sleep(2)
driver.close()
driver.switch_to.window(windowIds[0])
driver.find_element(By.XPATH,"//a[normalize-space()='Open New Seperate Windows']").click()
time.sleep(5)"""
#Approch2
driver.find_element(By.XPATH,"//a[@target='_blank']/button").click()
time.sleep(2)
windowIds = driver.window_handles
for window in windowIds:
    driver.switch_to.window(window)
    print(driver.title)
    