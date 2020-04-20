import os, sys
sys.path.append(os.getcwd())
from base.base_driver import get_driver
from pages.network_page import NetworkPage


class TestNetwork:
    def setup_class(self):
        self.driver = get_driver()
        self.network_page = NetworkPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_network(self):
        self.network_page.click_wifi_switch()
        self.network_page.click_mobile_network_button()
        self.network_page.click_mobile_data_switch()
        self.network_page.click_back_button()
        self.network_page.click_back_button()