"""import pytest
from selenium import webdriver
from data.urls import Urls

from web_locators import UIWorkerLocators
from pages import UIWorkerWeb


@pytest.fixture(params=['chrome', 'firefox'])
def driver_do(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get(Urls.MAIN_PAGE)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
        driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def pages(driver_do):
    driver = driver_do
    pages = UIWorkerWeb(driver, UIWorkerLocators())
    return pages

@pytest.fixture(scope='function')
def login(pages):
    pages.login()
    """

from web_locators import UIWorkerLocators
from pages import UIWorkerWeb
import pytest
from selenium import webdriver
from data.urls import Urls

from selenium.webdriver.chrome.options import Options


@pytest.fixture(params=["firefox", "chrome"])
def driver_do(request):
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome()
    
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def pages(driver_do):
    driver = driver_do
    pages = UIWorkerWeb(driver, UIWorkerLocators())
    return pages

@pytest.fixture(scope='function')
def login(pages):
    pages.login()