import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.constants import user_agent


@pytest.fixture(scope="function")
def driver():
    chrome_service = Service(ChromeDriverManager().install())
    chrome_options = ChromiumOptions()
    chrome_options.add_argument(
        f"user-agent={user_agent}"
    )
    driver = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def faker():
    return Faker()
