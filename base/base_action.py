from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver
        # self.driver.implicitly_wait(3)

    def input_text(self, by, loc, text):
        self.find_element(by, loc).send_keys(text)

    def click(self, by, loc):
        self.find_element(by, loc).click()

    def find_element(self, by, loc):
        return WebDriverWait(self.driver, 3, 0.5).until(lambda x: x.find_element(by, loc))

    def find_elements(self, by, loc):
        return WebDriverWait(self.driver, 3, 0.5).until(lambda x: x.find_elements(by, loc))