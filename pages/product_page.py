from base.base_page import BasePage
from base.locators import Locators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_product(self):
        self.click(Locators.PRODUCTION)

    def click_comment(self):
        element = self.is_visible(Locators.COMMENTS)
        if element:
            self.click(Locators.COMMENTS)
        else:
            print("No comments")

    def hover_comment(self):
        self.hover_to(Locators.HOVER)

    def click_accept_btn(self):
        self.click(Locators.TEXT_YES)
