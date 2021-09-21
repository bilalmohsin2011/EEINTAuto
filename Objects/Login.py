import time
from behave import *
import self as self
from Pages.LoginPageFactory import LoginPageFactory
from Utilities.BasePage import BasePage
from selenium import webdriver
from Utilities.SetUp import Setup

driver = Setup.driver


class LoginObject(BasePage):

    def openBrowser(self):
        Setup

    def enterUsername(uname):
        uname_field = driver.find_element_by_xpath(LoginPageFactory.username_XPATH)
        BasePage.wait_for_element_present(self, uname_field, 5)
        uname_field.send_keys(uname)

    def enterPassword(password):
        password_field = driver.find_element_by_xpath(LoginPageFactory.password_XPATH)
        BasePage.wait_for_element_present(self, password_field, 5)

        password_field.send_keys(password)

    def clickSubmit(self):
        driver.find_element_by_xpath(LoginPageFactory.submit_XPATH).click()
        time.sleep(5)

    def quit(self):
        driver.quit()
