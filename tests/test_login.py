from selenium import webdriver
import time

import config


class TestLogIn:

    def test_login(self, driver):
        driver.find_element_by_class_name("login").click()
        driver.find_element_by_id("email").send_keys(config.email)
        driver.find_element_by_id("passwd").send_keys(config.password)
        driver.find_element_by_id("SubmitLogin").click()
        time.sleep(5)
