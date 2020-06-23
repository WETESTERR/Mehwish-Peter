from selenium import webdriver

import config


class TestLogin:

    def test_login(self, driver, email, password):
        driver.find_element_by_class_name("login").click()
        email = driver.find_element_by_id("email").send_keys(email)  # fixture method should have same name everywhere. e.g. email,pasword, browser
        password = driver.find_element_by_id("passwd").send_keys(password)
        driver.find_element_by_id("SubmitLogin").click()
