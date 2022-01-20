from .base_page import BasePage
from .c_sharp_cource_page import CSharpCourcePage


class DashboardPage(BasePage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)

        self.__search_bar_locator = "//input[@id='search2']"
        self.__search_button_locator = "//button[@id='learntocode_searchbtn']"
        self.__sharp_course_element = "//h2[text()='C#']"

    def select_c_sharp_course(self) -> CSharpCourcePage:
        self._click_on_element(self.__sharp_course_element)

        return CSharpCourcePage(self._driver)
