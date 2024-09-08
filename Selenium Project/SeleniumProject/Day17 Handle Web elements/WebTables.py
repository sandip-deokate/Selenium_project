from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeDriverService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome(service=ChromeDriverService(ChromeDriverManager(driver_version="").install()))
driver.get("https://testautomationpractice.blogspot.com/")
#Find rows and colums
Rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
col = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

print(Rows,col)

#read spefic row and column data
"""for i in range(1,col+1):
    Rowdata=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[1]/th["+str(i)+"]").text
    print(Rowdata)
colnum =2
for i in range(1,Rows+1):
    if i==1:
        ColData=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(i) + "]/th[" + str(colnum) + "]").text
        print(ColData)
    else:
        ColData = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[" + str(i) + "]/td[" + str(colnum) + "]").text
        print(ColData)"""

#read all rows and colunm data
"""for i in range (1,Rows+1,1):
    for j in range (1,col+1,1):
        if i==1:
            Rowdata = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(i)+"]/th["+str(j)+"]").text
            print(Rowdata,end=" , ")
        else:
            Rowdata = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(i)+"]/td["+str(j)+"]").text
            if j<4:
                print(Rowdata,end=" , ")
            else:
                print(Rowdata, end="")

    print("\n")"""
#Read data base on condition (print Book name whose authername is mukesh)
"""for i in range (2,Rows+1,1):
    for j in range (2,3):
        Rowdata = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(i)+"]/td["+str(j)+"]").text
        if "Mukesh"==Rowdata:
            Bookname=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(i) + "]/td[1]").text
            print(Bookname,  Rowdata)"""
# print Book and price name whose authername is mukesh
for i in range(2,Rows+1):
    for j in range(2,3):
        Authername=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]/td["+str(j)+"]").text
        if Authername=="Amit":
            Bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]/td[1]").text
            BookPrice=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]/td[4]").text
            print(Bookname,Authername,BookPrice )









