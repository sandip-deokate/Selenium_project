from selenium import  webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
#service_obj = Service(executable_path=r"C:\Udemycourses\selenium\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version="127.0.6533.73").install()))

from selenium.webdriver.common.by import By

"""driver.get("https://demo.nopcommerce.com/")
time.sleep(2)
driver.find_element(By.ID,"small-searchterms").send_keys("Laptop")
#driver.find_element(By.CSS_SELECTOR,"form#small-search-box-form > .button-1.search-box-button").click()
time.sleep(2)
#driver.find_element(By.LINK_TEXT,"Computers").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Comp").click()
time.sleep(5)
driver.get("https://www.arrow.com")
slider= driver.find_elements(By.CLASS_NAME,"BannerHome--content-controlItem")
print("SliderCount:", len(slider))
linkCount=driver.find_elements(By.TAG_NAME,"a")
print("LinkCount: ",len(linkCount))"""
###############################################################
#CSS selector
# Tagname and Id
driver.get("https://www.facebook.com/")
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc") #tag name is optio nal

##Tagname and class
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("sandip")

#Tag and attribute
driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("deokate")
#Tag, class and attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("shreya")
#********************************* X-path  *********************

#driver.find_element(By.XPATH,"//html[@id='facebook']//input[@id='pass']").send_keys("ravan") #absolute
driver.find_element(By.XPATH,"//input[@data-testid='royal_pass']").send_keys("password")
#and
driver.find_element(By.XPATH,"//input[@name='email' and @data-testid='royal_email']").send_keys("Good")
driver .find_element(By.XPATH,"//input[@name='email' or @data-testid='royalemail']").clear()
driver.find_element(By.XPATH,"//input[contains(@name,'ema')]").send_keys("contains")
driver.find_element(By.XPATH,"//input[starts-with(@name,'ema')]").send_keys("all fine")
driver.find_element(By.XPATH," //button[text()='Log In']").click()
time.sleep(5)
