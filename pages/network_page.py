from appium.webdriver.common.mobileby import MobileBy
from base.base_action import BaseAction


class NetworkPage(BaseAction):
    network_button = MobileBy.XPATH, '//*[@text="Network & internet"]'
    back_button = MobileBy.ANDROID_UIAUTOMATOR, 'description("Navigate up")'
    wifi_switch = MobileBy.ANDROID_UIAUTOMATOR, 'description("Wi‑Fi")'
    mobile_network_button = MobileBy.ANDROID_UIAUTOMATOR, 'text("Mobile network")'
    mobile_data_switch = MobileBy.ANDROID_UIAUTOMATOR, 'className("android.widget.Switch").instance(0)'

    def __init__(self, driver):
        super().__init__(driver)
        self.click_network()

    def click_network(self):
        self.click(*self.network_button)

    def click_back_button(self):
        self.click(*self.back_button)

    def click_wifi_switch(self):
        self.click(*self.wifi_switch)

    def click_mobile_network_button(self):
        self.click(*self.mobile_network_button)

    def click_mobile_data_switch(self):
        self.click(*self.mobile_data_switch)