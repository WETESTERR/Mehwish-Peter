import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from webdriver_manager import driver

from utilities import driver_factory
import config


class Common:  # class name is always capital

    def __init__(self, driver):
        self.driver = driver

    def clicking(self, element):
        self.driver.find_element(element).click()

    def enter_text(self, element):
        self.driver.find_element(element).send_keys()

    def dropdown_Value(self, name):
        Select(self.driver.find_element_by_visible_text(name))

    def dropdown_index(self, index_number):
        Select(self.driver.find_element_by_index(index_number))

    def dropdown_option(self, text):
        Select(self.driver.find_element_by_value(text))

    actions = ActionChains(driver)

    def doubleclick(self, element):
        self.actions.double_click(driver.find_element(element).perform())

    def hoverover_an_object(self, element):
        self.actions.move_to_element(driver.find_element(element).perform())
