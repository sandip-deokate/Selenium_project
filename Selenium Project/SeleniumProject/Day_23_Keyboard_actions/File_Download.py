import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
import os
download_dir = "C:\A11ty"
os.makedirs(download_dir, exist_ok=True)
def ChromeSetUp():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    #Preferences
    ops = webdriver.ChromeOptions()
    preference= {"download.default_directory":download_dir,
                 "download.prompt_for_download": False,
                 "download.directory_upgrade": True,  # Allow directory upgrade
                 "safebrowsing.enabled": True,  # Enable safe browsing
                 "profile.default_content_setting_values.notifications": 0,# Block notifications
                  }


    ops.add_experimental_option("prefs",preference)

    #Arguments
    #ops.add_argument("--headless")
    ops.add_argument("--disable-features=DownloadBubble,DownloadBubbleV2")
    ops.add_argument("--safebrowsing-disable-download-protection")
    ops.add_argument("start-maximized")
    ops.add_argument("--disable-popup-blocking")  # Disable pop-up blocking
    ops.add_argument("--disable-infobars")  # Disable infobars
    ops.add_argument("--start-maximized")  # Start maximized
    #ops.add_argument("--no-sandbox")  # Bypass OS security model
    ops.add_argument("--disable-dev-shm-usage")  #


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
    return driver

driver = ChromeSetUp()
driver.get("https://www.arrow.com/")
driver.find_element(By.XPATH,"//input[@name='q']").send_keys("bav")
act=ActionChains(driver)
act.key_down(Keys.ENTER).click().perform()
ele = driver.find_element(By.XPATH,"//*[@id='item1']//a[@aria-label=' PDF, opens in a new tab']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.execute_script("arguments[0].click();", ele)
time.sleep(10)
windowIds = driver.window_handles
print(windowIds)
#driver.switch_to.new_window(windowIds[1])
"""myalert=driver.switch_to.alert
myalert.accept()"""
print(driver.title)
#act.key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.TAB).key_up(Keys.TAB).click().perform()

driver.switch_to.window(windowIds[0])




driver.find_element(By.CSS_SELECTOR,"tr:nth-of-type(1) .BuyingOptions-purchase > input").send_keys("5458")
time.sleep(10)




