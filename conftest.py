import pytest
import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_history_page import OrderHistoryPage


@pytest.fixture()
def driver():
    service = webdriver.chrome.service.Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    options.add_argument("--window_size=1920,1080")
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.get_url(data.MAIN_URL)
    return page


@pytest.fixture()
def profile_page(driver):
    page = ProfilePage(driver)
    return page


@pytest.fixture()
def order_history_page(driver):
    page = OrderHistoryPage(driver)
    return page
