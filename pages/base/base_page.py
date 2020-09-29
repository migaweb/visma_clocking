from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    url = None

    def __init__(self, driver, full_url):
        self.driver = driver
        self.url = full_url

    def go(self):
        self.driver.get(self.url)
        return None

    def alert_dismiss(self):
        Alert(self.driver).dismiss()
        return None

    def alert_accept(self):
        Alert(self.driver).accept()
        return None

    def wait_for_ajax(self):
        wait = WebDriverWait(self.driver, 15)
        try:
            wait.until(lambda driver: self.driver.execute_script(
                'return jQuery.active') == 0)
            wait.until(lambda driver: self.driver.execute_script(
                'return document.readyState') == 'complete')
        except Exception:
            pass
