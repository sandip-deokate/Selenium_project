import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys

driver= webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="128.0.6613.138").install()))
driver.get("https://text-compare.com/")
driver.maximize_window()
ele1 =driver.find_element(By.XPATH,"//*[@id='inputText1']")
ele2 = driver.find_element(By.XPATH,"//*[@id='inputText2']")

ele1.send_keys("hellooooo")

act = ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)
pates =ele2.text
print(pates)







