from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="127.0.6533.89").install()))
from selenium.webdriver.common.by import By
driver.get("https://demo.nopcommerce.com")

elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))
print(elements[0].text)   
for ele in elements:
    print(ele.text)
