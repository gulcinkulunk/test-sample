import unittest

from selenium import webdriver

from base.data import Data
from pages.home_page import HomePage
from pages.product_page import ProductPage
from base.locators import Locators


# Base Class for the tests
class TestCheckSearchApiBase(unittest.TestCase):
    """ Test case is:
      1. Open the browser, navigates to homepage
      2. Searching a product from search label
      3. Click to product on category page and go to product details
      4. Hover to comments button and click comments button
      5. Click to "yes" button on the comments label
      6. Check the "Thank you" message and close driver
      """

    def setUp(self):
        # Chrome run with driver
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(Data.CHROME_EXECUTABLE_PATH, options=chrome_options)
        # browser opens maximized window
        self.driver.maximize_window()


class TestCheckSearchApi(TestCheckSearchApiBase):
    def setUp(self):
        super().setUp()

    def test_check_search_api_case(self):
        #  opens the browser and navigates to homepage
        self.homePage = HomePage(self.driver)
        # equals control title on homepage
        self.assertIn(Data.HOME_PAGE_TITLE, self.homePage.driver.title)
        self.homePage = HomePage(self.driver)
        # search the product on homepage
        self.homePage.search()
        self.productDetailsPage = ProductPage(self.driver)
        # click product and shows product details
        self.productDetailsPage.click_product()
        # click comments on product details
        self.productDetailsPage.click_comment()
        # click accept button
        self.productDetailsPage.click_accept_btn()
        # check to text on comments
        self.assertTrue(Locators.TEXT_THANKS, Data.THANKS_TEXT)


def tearDown(self):
    # To do the cleanup after test has executed.
    self.driver.close()
    self.driver.quit()
