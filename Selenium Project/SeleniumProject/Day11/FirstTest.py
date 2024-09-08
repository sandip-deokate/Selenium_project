"""Test Case
-----------
1) Open Web Browser(Chrome/firefox/Edge).
2) Open URL  https://opensource-demo.orangehrmlive.com/
3) Enter username  (Admin).
4) Enter password  (admin123).
5) Click on Login.
6) Capture title of the home page.(Actual title)
7) Verify title of the page: OrangeHRM    (Expected)
8) close browser"""
import time

#________________________________________________________
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Driver= webdriver.Chrome(service = ChromeService(ChromeDriverManager(driver_version='127.0.6533.73').install()))
Driver.get("https://www.arrow.com/")
Driver.maximize_window()
Driver.find_element(By.CSS_SELECTOR,".Header-navBar.Header-topLinks.row a[title='Login'] > .head-uppercase").click()
element=Driver.find_element(By.CSS_SELECTOR,"input#username").send_keys("sandipprod@mailsac.com")
if element is not None:
    print("element found")
else:
    print("")
Driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("Arrow@123456")
Driver.execute_script("window.scrollTo(0,window.scrollY+200)")
Driver.find_element(By.CSS_SELECTOR,"form#loginForm  button > span").click()
try:
    element = WebDriverWait(Driver,50).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,".Header-navBar.Header-topLinks.row div[title='My Account']")))
    actTitle = element.get_attribute("title")
    print("Actual Title", actTitle)
except:
    print("element not fount")

#actTitle= Driver.find_element(By.CSS_SELECTOR,".Header-navBar.Header-topLinks.row div[title='My Account']").get_attribute("title")
#print(actTitle)
Expected_Title = "My Account"
if actTitle == Expected_Title:
    print("User logged in successfully")
else:
    print("User not logged in successfully")


time.sleep(1)

#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#

