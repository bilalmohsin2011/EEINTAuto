import time
import driver as driver
import self as self
from behave import *
from selenium import webdriver
from Pages.LoginPageFactory import LoginPageFactory
from Objects.Login import LoginObject



class LogIn:

    @given('launch chrome browser')
    def launch_browser(context):
        LoginObject.openBrowser(self)

    @then('Verify that user enters username')
    def enter_username(context):
        LoginObject.enterUsername(LoginPageFactory.username_Test)

    @then('Verify user enters password')
    def enter_password(context):
        LoginObject.enterPassword(LoginPageFactory.password_Test)

    @then('user clicks on submit button')
    def click_submit(context):
        LoginObject.clickSubmit(self)
        time.sleep(3)
        LoginObject.quit(self)