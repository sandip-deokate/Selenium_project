from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="").install()))

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
drop=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']"))
"""drop.select_by_visible_text("1")
time.sleep(4)
drop.select_by_index(2)
time.sleep(2)
drop.select_by_value("3")
time.sleep(2)"""
#Print All options
allele= drop.options
print(len(allele))
for ele in allele:
    print(ele.text)




