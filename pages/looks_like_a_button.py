from pages.base_page import BasePage
from selenium.webdriver.common.by import By

button_selector = (By.XPATH, "//*[@class='a-button']")

class LooksButton(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get("https://www.qa-practice.com/elements/button/like_a_button")

    @property
    def button(self):
        return self.find(button_selector)

    @property
    def button_exist(self):
        return self.button.is_displayed