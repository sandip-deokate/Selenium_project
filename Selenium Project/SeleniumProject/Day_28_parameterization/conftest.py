
import pytest
from selenium import webdriver


#one driver
'''@pytest.fixture(scope="function")
def setup():
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    Driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    yield Driver
    Driver.quit()'''

# Multiple driver
@pytest.fixture(scope="function")
def setup(Browser):
    if Browser=="Chrome" or Browser=="chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager
        Driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        yield Driver
        Driver.quit()
    elif Browser == "edge" or Browser=="Edge":
        from selenium.webdriver.edge.service import Service as EdgeService
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        Driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        yield Driver
        Driver.close()

    elif Browser == "Firefox" or Browser=="firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        #Driver = webdriver.Firefox(service=FireService(GeckoDriverManager().install()))
        from selenium.webdriver.firefox.options import Options
        options = Options()
        # Provide Firefox binary location (if needed)
        options.binary_location = r"C:\Users\148350\AppData\Local\Mozilla Firefox\firefox.exe"
        Driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        return Driver

def pytest_addoption(parser): # this method captures value from command line
    parser.addoption("--Browser")

@pytest.fixture()
def Browser(request): # this will return value to setup method
    return request.config.getoption("--Browser")



