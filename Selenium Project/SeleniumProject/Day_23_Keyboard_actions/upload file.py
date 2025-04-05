import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException,NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


def ChromeSetup():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    ops =Options()
    #ops = webdriver.ChromeOptions()
    ops.add_argument("start-maximized")

    driver=webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="").install()),options=ops)
    return driver


driver = ChromeSetup()
my_wait = WebDriverWait(driver,30,poll_frequency=2)
driver.get("https://www.arrow.com/")

BomTool=my_wait.until(EC.presence_of_element_located((By.XPATH,"//a[@aria-label='BOM Tool']")))
driver.execute_script("arguments[0].click();", BomTool)
driver.find_element(By.XPATH,"//a[normalize-space()='Accept Terms']").click()
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("sandipprod@mailsac.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Arrow123456*")

Login=driver.find_element(By.XPATH,"//form[@id='loginForm']//span[.='Login']")
driver.execute_script("window.scrollBy(0,500)")
#driver.execute_script("arguments[0].scrollIntoView();",Login)
Login.click()
uploadBom = my_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".upload-box--button")))

uploadBom.send_keys("C:\A11ty\BomShortAndQuick.xlsx")
time.sleep(10)







