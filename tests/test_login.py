from page_objects.login import Login


class TestLogin:

    def test_login(self, driver, email, password):
        l = Login(driver)
        l.login(email, password)
        l.logout()


import time

from webdriver_manager import driver


class TestLogin():

    def test_login(self, driver, email, password):
        login = driver.find_element_by_class_name("login").click()
        email = driver.find_element_by_id("email").send_keys(
            email)  # fixture method should have same name everywhere. e.g. email,pasword, browser
        password = driver.find_element_by_id("passwd").send_keys(password)
        submit = driver.find_element_by_id("SubmitLogin").click()

    def test_logout(self, driver, logout):
        logout = driver.find_element_by_class_name("logout").click()
        return logout
