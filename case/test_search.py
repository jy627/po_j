import time

import pytest

from read_data.read_yaml import build_data_func
from page.page_factory import PageFactory

from utils import get_driver


class TestSearch(object):
    @pytest.fixture(autouse=True)
    def before_func(self):
        self.driver = get_driver()
        self.page_factory = PageFactory(self.driver)
        yield
        time.sleep(3)
        self.driver.quit()


    @pytest.mark.parametrize("text",build_data_func())
    def test_func(self,text):
        # self.index_page = IndexPage(self.driver)
        # self.index_page.click_search_btn()
        #
        # self.search_page = SearchPage(self.driver)
        # self.search_page.input_search_bar("黑马程序员")
        self.page_factory.index_page().click_search_btn()
        self.page_factory.search_page().input_search_bar(text)


















