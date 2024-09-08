import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="").install()))

myWait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#myWait.until(EC.presence_of_element_located(By.XPATH))

#Approch 1 find number of links of webpage

"""links = driver.find_elements(By.XPATH,"//a")
print(len(links))

#Print all links name

for link in links:
    print(link.text)"""

#Broken link
driver.get("http://www.deadlinkcity.com/")
links=driver.find_elements(By.XPATH,"//a")
print(len(links))
for link in links:
    try:
        url=link.get_attribute("href")
        res=requests.head(url)
    except:
        var = None
    if res.status_code >=400:
        print(url," Broken kink")
    else:
        print(url," valid link")