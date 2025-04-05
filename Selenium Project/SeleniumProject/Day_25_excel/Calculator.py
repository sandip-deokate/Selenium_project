import time
from importlib import import_module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import excel_Operations

def Chrome():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    driver=webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="").install()))
    driver.maximize_window()
    return driver

driver=Chrome()
filePath="C:\\Udemycourses\\GitandGitHub\\Selenium Project\\SeleniumProject\\Day_25_excel\\caldata.xlsx"
sheetName="Sheet1"

maxRowCount=excel_Operations.getRowCount(filePath,sheetName)
maxColCount=excel_Operations.getColCount(filePath,sheetName)
print(maxRowCount,maxColCount)


class calculate():
    def calculateInterestRate(self,principleAmount,rateOfInterest,periodValue,periodUnit):
        driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
        Principle = driver.find_element(By.XPATH, "//input[@id='principleAmount']")
        Principle.clear()
        Principle.send_keys(principleAmount)

        Annual_Rate=driver.find_element(By.XPATH,"//input[@id='annualrate']")
        Annual_Rate.clear()
        Annual_Rate.send_keys(rateOfInterest)

        PeriodValue= driver.find_element(By.XPATH,"//input[@id='periodInDigit']")
        PeriodValue.clear()
        PeriodValue.send_keys(periodValue)

        drop=Select(driver.find_element(By.XPATH,"//select[@name='periodUnit']"))
        drop.select_by_value(periodUnit)

        total= driver.find_element(By.XPATH,"//div[text()='Total Value']/following-sibling::div/span[2]")
        totalAmount = total.text
        return totalAmount

class excel():
    def getExcelData(self):
            for i in range(2,maxRowCount+1):
                for j in range(1,maxColCount+1):
                    row=i
                    col=j
                    if col==1:
                        principleAmount= excel_Operations.readFile(filePath,sheetName,row,col)
                    elif col==2:
                        rateOfInterest=excel_Operations.readFile(filePath,sheetName,row,col)
                    elif col==3:
                        periodValue=excel_Operations.readFile(filePath,sheetName,row,col)
                    elif col==4:
                        periodUnit= excel_Operations.readFile(filePath,sheetName,row,col)
                    elif col==5:
                        Frequency= excel_Operations.readFile(filePath,sheetName,row,col)

                calc = calculate()
                total=(calc.calculateInterestRate(principleAmount,rateOfInterest,periodValue,periodUnit))

                total1 = total.replace(",","")
                maturityValue= excel_Operations.readFile(filePath,sheetName,i,6)
                if total1==maturityValue:
                    excel_Operations.writeFile(filePath,sheetName,i,7,"PASS")
                    excel_Operations.fillGreenColor(filePath,sheetName,i,7)
                    excel_Operations.writeFile(filePath, sheetName, i, 8, total1)
                else:
                    excel_Operations.writeFile(filePath, sheetName, i, 7, "Fail")
                    excel_Operations.fillRedColor(filePath, sheetName, i, 7)
                    excel_Operations.writeFile(filePath, sheetName, i, 8, total1)

E=excel()
E.getExcelData()














