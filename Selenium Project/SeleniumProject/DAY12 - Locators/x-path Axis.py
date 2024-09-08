import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version='127.0.6533.73').install()))
driver.maximize_window()
driver.get("https://money.rediff.com/gainers")
driver.execute_script("window.scrollTo(0,window.scrollY+600)")
time.sleep(5)
#Self
V =driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/self::a").text
print(V)
#parent
a=driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/parent::td").text
print(a)
b=driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/parent::td/following-sibling::td[4]").text
print(b)

#acestor
c= driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/ancestor::tr").text
print(c)
#acestor following -
d=driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/ancestor::tr/following::tr[1]/td/a").text
print("d=",d)

#descendant
e = driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/ancestor::tbody/descendant::tr[2]").text
print(e)

#following
f =driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/ancestor::tr/following::tr/td/a").text
print("following",f)

#following sibling
h=driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/ancestor::tr/following-sibling::tr").text
print(h)
g=driver.find_elements(By.XPATH,"//a[contains(text(),'Sudarshan')]/ancestor::tr/following-sibling::tr")
print(len(g))

#preceding
i=driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/ancestor::tr/preceding::tr[1]").text
print("preceding",i)

#preceding sibling -
k= driver.find_element(By.XPATH,"//a[contains(text(),'Sudarshan')]/ancestor::tr/preceding-sibling::tr[1]").text
print(k)