from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import config


class Driver:
    def launch_url(self, browser):
        driver = None
        browser_lower = browser.lower() #lower() is a methodwhch
        if browser_lower == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser_lower == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_lower == "ie":
            driver = webdriver.Ie(IEDriverManager().install())
        elif browser_lower == "opera":
            driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        elif browser_lower == "edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver.get(config.url)
        driver.maximize_window()
        return driver

    def quit_driver(self, driver):
        driver.quit_driver()

