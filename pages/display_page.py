from appium.webdriver.common.mobileby import MobileBy
from base.base_action import BaseAction


class DisplayPage(BaseAction):
    display_button = MobileBy.XPATH, '//*[@text="Display"]'
    search_button = MobileBy.ACCESSIBILITY_ID, 'Search settings'
    search_text = MobileBy.ID, 'android:id/search_src_text'
    back_button = MobileBy.ACCESSIBILITY_ID, 'Navigate up'

    def __init__(self, driver):
        super().__init__(driver)
        self.click_display()

    def click_display(self):
        self.click(*self.display_button)

    def click_search_button(self):
        self.click(*self.search_button)

    def input_search_text(self, text):
        self.input_text(*self.search_text, text)

    def click_back_button(self):
        self.click(*self.back_button)