from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeDriverService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
ops= webdriver.ChromeOptions
#ops.add_argument("--disable-notifications")
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Chrome(service=ChromeDriverService,options=ops(ChromeDriverManager().install()))
driver.get("https://www.gps-coordinates.net/my-location")
time.sleep(5)




