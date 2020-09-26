from selenium.webdriver.common.by import By

from page_objects.common import Common


class Login(Common):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    email_textbox = "email"
    password_textbox = "password"
    signIn_tab = driver.find_element_by_class_name("login").click()
    submit = driver.find_element_by_id("SubmitLogin")
    logout_button = (By.CLASS_NAME, "logout")

    def login(self, email, password):
        self.clicking(Login.email_textbox)
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_id(Login.email_textbox).send_keys(email)
        self.driver.find_element_by_id(Login.password_textbox).send_keys(password)
        self.submit.click()

    def logout(self):
        self.logout_button.click()
