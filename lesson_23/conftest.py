import pytest

from selenium.webdriver import Chrome

from lesson_23.pages.dashboard_page import DashboardPage


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("./core/infrastructure/bin/chromedriver")
    driver.get("https://www.w3schools.com")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def dashboard_page(driver):
    yield DashboardPage(driver)
