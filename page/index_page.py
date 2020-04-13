from selenium.webdriver.common.by import By
import page

from base.base_page import BasePage


class IndexPage(BasePage):
    # search_btn = (By.ID,"com.android.settings:id/search")

    def click_search_btn(self):

        # self.find_element_func(self.search_btn).click()
        # self.click_func(self.find_element_func(self.search_btn))
        self.click_func(self.find_element_func(page.search_btn))
