from selenium.webdriver.common.by import By

from page_objects.common import Common


class Login(Common):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    email_textbox = "email"
    password_textbox = "password"
    sign_in_button = "login"
    sign_in_submit_button = "SubmitLogin"
    sign_out_button = "logout"

##Verufy the locators id, class or classname

    def login(self, email, password):
        self.click(Login.sign_in_button,"id")
        self.enter_text(Login.email_textbox,"id",email)
        self.enter_text(Login.password_textbox , "",password)
        self.click(Login.sign_in_submit_button,"")
        self.verify_element_present(Login.sign_out_button,"")
        #Put successful Login logs

    def logout(self):
        self.click(Login.sign_out_button,"")
        self.verify_element_present(Login.sign_in_button,"")
        #Successful Logout logs
