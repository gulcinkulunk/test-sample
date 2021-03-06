from base.base_page import BasePage
from base.data import Data
from base.locators import Locators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Data.BASE_URL)

    def search(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()
        self.enter_text(Locators.SEARCH_TEXTBOX, Data.SEARCH_KEYWORD)
        self.click(Locators.SUBMIT_BUTTON)
