from selenium import webdriver
def ChromeSetUp():
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

driver = ChromeSetUp()
driver.get("https://www.google.com/")