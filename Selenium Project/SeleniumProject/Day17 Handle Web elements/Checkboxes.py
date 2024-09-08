from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="127.0.6533.89").install()))

mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,Exception])


driver.get("https://www.globalsqa.com/samplepagetest/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//input[@value='Functional Testing']").click()
elements=driver.find_elements(By.XPATH,"//label[@class='grunion-field-label']/following::input[@type='checkbox']")
#Approch 1
"""for ele in elements:
    ele.click()
"""

#Approch two
"""for ele in elements:
    x = ele.get_attribute('value')
    print(x)
    if x == "Functional Testing" or x=="Manual Testing":
        ele.click()
    else:
        pass"""

#Approch 3 select last two element
"""for i in range(1,len(elements)):
    elements[i].click()
"""

#Approch 4 select first two checkbox
"""for i in range(0,len(elements)-1):
    elements[i].click()"""
time.sleep(5)
