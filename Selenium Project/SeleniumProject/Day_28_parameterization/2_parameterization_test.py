from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


class TestClass:
    def test_Login_arrow_website(self,setup):
        self.Driver = setup
        self.Driver.get("https://www.arrow.com/")
        self.Driver.maximize_window()
        time.sleep(2)
        self.Driver.find_element(By.CSS_SELECTOR,
                                 ".Header-navBar.Header-topLinks.row a[title='Login'] > .head-uppercase").click()
        self.element = self.Driver.find_element(By.CSS_SELECTOR, "input#username").send_keys("sandipprod@mailsac.com")
        if self.element is not None:
            print("element found")
        else:
            print("")
        self.Driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("Arrow@123456")
        self.Driver.execute_script("window.scrollTo(0,window.scrollY+200)")
        self.Driver.find_element(By.CSS_SELECTOR, "form#loginForm  button > span").click()
        try:
            element = WebDriverWait(self.Driver, 50).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".Header-navBar.Header-topLinks.row div[title='My Account']")))
            self.actTitle = element.get_attribute("title")
            print("Actual Title", self.actTitle)
        except:
            print("element not fount")
        Expected_Title = "My Account"
        if self.actTitle == Expected_Title:
            print("User logged in successfully")
        else:
            print("User not logged in successfully")
