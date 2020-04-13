"""
PO文件基类

"""
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def find_element_func(self,location,timeout=5,poll=.5):

        """元素定位方法"""

        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).\
            until(lambda  x : x.find_element(location[0],location[1]))
        # return self.driver.find_element(location[0],location[1])
        return element

    def input_func(self,element,text):

        element.clear()
        element.send_keys(text)



    def click_func(self,element):

        element.click()





































