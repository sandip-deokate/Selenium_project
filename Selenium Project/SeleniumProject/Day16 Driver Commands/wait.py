import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException,ElementNotSelectableException
driver =webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="127.0.6533.89").install()))
driver.implicitly_wait(10)#seconds
driver.get("https://www.google.com")
ele=driver.find_element(By.XPATH,"//textarea[@aria-label='Search']")
ele.send_keys("selenium")
ele.submit()
#driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

#my_wait=WebDriverWait(driver,20) #Basic syntax
my_wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                        ElementNotVisibleException,
                                                        ElementNotSelectableException,
                                                                                    ])
searchlink=my_wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()
print("excuted successfully")
time.sleep(5)
driver.quit()

