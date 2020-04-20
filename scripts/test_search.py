import os, sys
sys.path.append(os.getcwd())
from base.base_driver import get_driver
from pages.search_page import SearchPage
from base.base_yaml import get_yaml_data
import pytest

def data_with_key(key):
    return get_yaml_data('search_data')[key]


class TestSearch:
    def setup_class(self):
        self.driver = get_driver()
        self.search_page = SearchPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('content', data_with_key('test_search'))
    def test_search(self, content):
        self.search_page.click_search_box()
        self.search_page.input_search_text(content)
        self.search_page.click_back_button()