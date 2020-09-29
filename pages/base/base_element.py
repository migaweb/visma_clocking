
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)

    def input_clear(self):
        self.web_element.clear()

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None
    
    def is_enabled(self):
        return self.web_element.is_enabled()

    @property
    def text(self):
        text = self.web_element.text
        return text
