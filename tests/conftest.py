import pytest

import config
from tests.test_login import TestLogIn
from utilities.driver_factory import Driver

d = Driver()  # Created an instance
loginep = TestLogIn()


@pytest.fixture(scope="session")
def driver(browser):
    driver = d.launch_url(browser)
    # todo, teardown
    return driver


@pytest.fixture(scope="session", autouse=True)  # autouse will help to run the test case automatically
def browser(request):
    return request.config.getoption("--browser")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--email")
    parser.addoption("--password")


@pytest.fixture(scope="session", autouse=True)
def email(request):
    return request.config.getoption("--email")


@pytest.fixture(scope="session", autouse=True)
def password(request):
    return request.config.getoption("--password")
