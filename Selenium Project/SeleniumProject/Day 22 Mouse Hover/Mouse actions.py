import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="128.0.6613.120").install()))
act = ActionChains(driver)

"""driver.get("https://www.globalsqa.com/samplepagetest/")
driver.maximize_window()
ele=driver.find_element(By.XPATH,"//a[normalize-space()='Tester’s Hub']")
act = ActionChains(driver)
#act.move_to_element(ele).perform()
ele1= driver.find_element(By.XPATH,"//a[normalize-space()='AngularJS Protractor Practice Site']")
act.move_to_element(ele).move_to_element(ele1).click().perform()
time.sleep(2)"""

"""driver.get("https://the-internet.herokuapp.com/context_menu")
driver.maximize_window()
act =ActionChains(driver)
ele1=driver.find_element(By.XPATH,"//*[@id='hot-spot']")
act.context_click(ele1).perform()
Alert=driver.switch_to.alert
Alert.accept()
print("Code successfully excuted")"""

#Drag and grop

"""act =ActionChains(driver)
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
ele3= driver.find_element(By.ID,"column-b")
ele2= driver.find_element(By.ID,"column-a")
act.drag_and_drop(ele2,ele3).perform()
time.sleep(10)
"""

#Slider
driver.get("https://the-internet.herokuapp.com/horizontal_slider")
ele = driver.find_element(By.XPATH, "//input[@type='range']")
print("intial location", ele.location)

act.drag_and_drop_by_offset(ele, 2, 0).perform()
print("final location", ele.location)
time.sleep(10)
