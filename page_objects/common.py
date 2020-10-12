import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from webdriver_manager import driver

from utilities import driver_factory
import config
from utilities.log import Logger
class Common:  # class name is always capital


    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, strategy):  #Stretgy = string, id, css (selenium)
        if strategy == "id":
            return self.driver.find_element_by_id(locator)
        elif strategy == "name":
            return  self.driver.find_element_by_name(locator)
        elif strategy == "css_selector":
            return self.driver.find_element_by_css_selector(locator)
        elif strategy == "class_name":
            return  self.driver.find_element_by_class_name(locator)
        elif strategy == "xpath":
            return self.driver.find_element_by_xpath(locator)
        elif strategy == "link_text":
            return self.driver.find_element_by_link_text(locator)
        elif strategy == "partial_link_text":
            return self.driver.find_element_by_partial_link_text(locator)
        else:
            pytest.fail("Given strategy is not valid {}".format(strategy))

# Assignment = Write methods using the get element.


    def click(self, locator ,strategy):
        element = self.get_element(locator,strategy)
        if element:                     #If variable or element is not empty
            element.click()
            #We have to put Logging here
        else:
            # We have to put Logging here
            pytest.fail("Failed to click on the element {}" .format(locator))


    def enter_text(self,locator, strategy):
        element = self.get_element(locator, strategy)
        if element:
            element.Send_Keys()
            # We have to put Logging here
        else:
            #We have to put Logging here
            pytest.fail("Failed to enter text {}" .format(locator))


    def get_elements(self,strategy,locator):
        if strategy == "id":
            return self.driver.find_elements_by_id(locator)
        elif strategy == "name":
            return self.driver.find_elements_by_name(locator)
        elif strategy == "css":
            return self.driver.find_elements_by_css_selector(locator)
        elif strategy == "xpath":
            return self.driver.find_elements_by_xpath(locator)
        elif strategy == "class_name":
            return  self.driver.find_elements_by_class_name(locator)
        elif strategy == "link_text":
            return self.driver.find_elements_by_link_text(locator)
        elif strategy == "partial_link_text":
            return self.driver.find_elements_by_partial_link_text(locator)
        else:
            pytest.fail("Given strategy is not valid {}".format(strategy))

    def selection_from_drop_down_menu(self, locator, strategy):
        if strategy == "dropdown_text":
            return Select(self.driver.find_element_by_visible_text(locator))
        elif strategy == "dropdown_index":
            return Select(self.driver.find_element_by_index(locator))
        elif strategy == "dropdown_value":
            return Select(self.driver.find_element_by_value(locator))
        else:
            pytest.fail("Given strategy is not valid {}".format(strategy))

    def clear_text(self, locator, strategy):
        element = self.get_element(locator, strategy)
        if element:
            element.clear()
            # We have to put Logging here
        else:
            # We have to put Logging here
            pytest.fail("Failed to click on the element {}".format(locator))

    def verify_exact_element(self, locator,strategy, validatetext):
        element =  self.get_element(locator,strategy)
        if element:
            gettext = element.text
            assert validatetext == gettext
            #Log text for validation
        else:
            pytest.fail("Element not found {}" .format(strategy))

    def time_sleep(self, sleep_time):
        time.sleep(sleep_time)

    def wait(self, wait_time):
        WebDriverWait(self.driver, wait_time)  #Not sure why Webdriver is here?

    def verify_text_present(self,locator,strategy,validatetext):
        element = self.get_element(locator, strategy)
        if element:
            gettext = element.text
            assert validatetext == gettext
            # Log text for validation
        else:
            pytest.fail("Element not found {}".format(strategy))

    def switch_frame(self, value):
        self.driver.switch_to.frame(value)

    def switch_alert(self, value):
        self.driver.switch_to.alert(value)

    def switch_window(self, value):
        self.driver.switch_to.window(value)


log = Logger()
