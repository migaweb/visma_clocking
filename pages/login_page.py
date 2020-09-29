# Username, Password, LoginButton

from selenium.webdriver.common.by import By
from pages.base.locator import Locator
from pages.base.base_page import BasePage
from pages.base.base_element import BaseElement


class LoginPage(BasePage):

    @property
    def get_username_input(self):
        locator = Locator(By.ID, value='Username')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def get_password_input(self):
        locator = Locator(By.ID, value='Password')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def get_save_button(self):
        locator = Locator(By.ID, value='LoginButton')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def get_calendar_button(self):
        locator = Locator(By.ID, value='mainService_timeclock')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def get_in_button(self):
        locator = Locator(By.ID, value='btn-in')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def get_out_button(self):
        locator = Locator(By.ID, value='btn-out')
        return BaseElement(driver=self.driver, locator=locator)