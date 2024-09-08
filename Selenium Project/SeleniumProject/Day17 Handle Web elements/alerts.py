from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()

#myalert=driver.switch_to.alert
"""print(myalert.text)
time.sleep(5)
myalert.accept()
time.sleep(5)"""
# text box
"""driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
myalert=driver.switch_to.alert
print(myalert.text)
myalert.send_keys("Alert hain kya tu")
time.sleep(5)
#myalert.accept() 
myalert.dismiss()
time.sleep(5)"""

#Authenticate popup
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)




