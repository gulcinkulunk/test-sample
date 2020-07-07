from selenium.webdriver.common.by import By


class Locators:
    SEARCH_TEXTBOX = (By.CLASS_NAME, "desktopOldAutosuggestTheme-input")
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='SearchBoxOld-buttonContainer']")
    PRODUCTION = (By.XPATH, "//*[contains(@class, 'not-fashion-flex')][2]")
    COMMENTS = (By.XPATH, "//*[contains(@class, 'product-comments')][1]")
    HOVER = (By.XPATH, "//a[@id='productReviewsTab']")
    TEXT_YES = (By.XPATH, "//div[contains(@class, 'ReviewCard')]//*[contains(text(), 'Evet')]")
    TEXT_THANKS = (By.XPATH, "//*[contains(text(), 'Teşekkür Ederiz.')]")
