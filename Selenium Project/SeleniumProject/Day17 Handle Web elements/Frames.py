from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element(By.XPATH,"//a[normalize-space()='Nested Frames']").click()
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
driver.find_elements(By.XPATH,"//body[normalize-space()='LEFT']")
print("I am Left")
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-middle")
print("I am middle")
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-right")
print("I am right")
driver.switch_to.default_content()# Switch to main frame
driver.switch_to.frame("frame-bottom")
print("I am bottom")


driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click()
oterframe=driver.find_element(By.XPATH,"//div[@id='Multiple']/iframe")
driver.switch_to.frame(oterframe)
inner=driver.find_element(By.XPATH,"//div[@class='iframe-container']/iframe")
driver.switch_to.frame(inner)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")
import time
time.sleep(5)

