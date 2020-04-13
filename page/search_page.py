
from selenium.webdriver.common.by import By

import page
from base.base_page import BasePage


class SearchPage(BasePage):

    # search_bar = (By.ID, 'android:id/search_src_text')

    search_bar = page.search_bar

    def input_search_bar(self, text):

        # self.find_element_func(self.search_bar).send_keys(text)
        # self.input_func(self.find_element_func(self.search_bar),text)
        self.input_func(self.find_element_func(page.search_bar), text)










