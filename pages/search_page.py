from appium.webdriver.common.mobileby import MobileBy
from base.base_action import BaseAction


class SearchPage(BaseAction):
    search_box = MobileBy.ID, 'com.android.settings:id/search_action_bar'
    search_input = MobileBy.ID, 'android:id/search_src_text'
    back_button = MobileBy.ACCESSIBILITY_ID, 'Navigate up'

    def __init__(self, driver):
        super().__init__(driver)

    def click_search_box(self):
        self.click(*self.search_box)

    def input_search_text(self, text):
        self.input_text(*self.search_input, text)

    def click_back_button(self):
        self.click(*self.back_button)