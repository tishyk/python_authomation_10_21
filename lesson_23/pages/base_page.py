from __future__ import annotations

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .singleton import Singleton


class BasePage(Singleton):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.__wait = WebDriverWait(self._driver, 15)
        self.__title_locator = "//div[@id='main']//h1"

    def _get_title(self, text: str) -> str:
        locator = f"{self.__title_locator}[contains(text(), '{text}')]"
        return self.__wait_element(locator).text

    def _click_on_element(self, by: str) -> None:
        element = self.__wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, by)
            )
        )
        element.click()

    def __wait_element(self, locator: str) -> WebElement:
        return self.__wait.until(
            EC.presence_of_element_located(
                (By.XPATH, locator)
            )
        )
