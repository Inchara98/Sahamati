from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from Utilities.readProperties import ReadConfig


@pytest.fixture()
def setup(browser):
    options = ChromeOptions() if browser == 'chrome' else FirefoxOptions()
    prefs = {'download.default_directory': ReadConfig.get_download_dir()}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("--window-size=3860,2160")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("prefs",
                                    {
                                        "download.default_directory": "Downloads"})

    if browser == 'chrome':
        driver = webdriver.Chrome(options=options)
        print("Launching chrome browser.......")
    elif browser == 'firefox':
        driver = webdriver.Firefox(options=options)
        print("Launching firefox browser.......")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
