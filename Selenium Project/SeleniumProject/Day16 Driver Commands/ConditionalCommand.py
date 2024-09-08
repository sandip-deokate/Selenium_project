from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version='127.0.6533.89').install()))

driver.get("https://demo.nopcommerce.com/register")
try:
    a=driver.find_element(By.XPATH,"//h1")
    print(a.is_displayed())
    b=driver.find_element(By.XPATH,"//button[@id='newsletter-subscribe-button']")
    print(b.is_displayed())
except:
    print("element is not displayed")
driver.maximize_window()
try:
    driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
    assert driver.find_element(By.XPATH,"//input[@id='gender-male']").is_selected()
except AssertionError:
    print("Assertion is failed")


