import os, sys
sys.path.append(os.getcwd())
from base.base_driver import get_driver
from pages.display_page import DisplayPage


class TestDisplay:
    def setup_class(self):
        self.driver = get_driver()
        self.display_page = DisplayPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_display(self):
        self.display_page.click_search_button()
        self.display_page.input_search_text('123')
        self.display_page.click_back_button()