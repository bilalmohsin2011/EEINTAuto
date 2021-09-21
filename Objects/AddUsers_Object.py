import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Objects.Login import LoginObject
from Pages.LoginPageFactory import LoginPageFactory
from Utilities.BasePage import BasePage
from Utilities.SetUp import Setup
from Pages.AddUsersFactory import AddUserFactory

driver = Setup.driver


class AddUsers(BasePage):
    def login(self):
        LoginObject.openBrowser(self)
        LoginObject.enterUsername(LoginPageFactory.username_Test)
        LoginObject.enterPassword(LoginPageFactory.password_Test)
        LoginObject.clickSubmit(self)

    def goToUsersScreen(self):
        BasePage.wait_for_element_present(self, driver.find_element_by_xpath(LoginPageFactory.dashboard_Xpath), 10)
        usersButton = driver.find_element_by_xpath(AddUserFactory.users_SideMenu_Xpath)
        usersButton.click()

    def clickAddNewUsers(self):
        time.sleep(3)
        BasePage.wait_for_element_visible(self, driver.find_element_by_xpath(AddUserFactory.addNewUserButton_Xpath), 10)
        addNewUser = driver.find_element_by_xpath(AddUserFactory.addNewUserButton_Xpath)
        addNewUser.click()

    def openAddUserForm(self):
        BasePage.wait_for_element_visible(self, driver.find_element_by_xpath(AddUserFactory.Explicit_AddUser_XPATH), 10)

    def enterFirstName(self):
        firstName = driver.find_element_by_xpath(AddUserFactory.fistName_Xpath)
        firstName.send_keys(AddUserFactory.FirstName)

    def enterLastName(self):
        lastName = driver.find_element_by_xpath(AddUserFactory.lastName_Xpath)
        lastName.send_keys(AddUserFactory.LastName)

    def enterEmail(self):
        email = driver.find_element_by_xpath(AddUserFactory.email_Xpath)
        email.send_keys(AddUserFactory.Email)

    def chooseFieldOperator(self):
        select = Select(driver.find_element_by_xpath(AddUserFactory.fieldOperator_XPATH))
        select.select_by_visible_text(AddUserFactory.role)

    def enterHourlyRate(self):
        time.sleep(3)
        hourlyRate = driver.find_element_by_xpath(AddUserFactory.hourlyRate_Xpath)
        hourlyRate.send_keys(AddUserFactory.HourlyRate)

    def submitUser(self):
        submitButton = driver.find_element_by_xpath(AddUserFactory.AddUserButton_Xpath)
        submitButton.click()
        time.sleep(10)

    def userDisplayed(self):
        userView = driver.find_element_by_xpath(AddUserFactory.emailView_XPATH)
        print(BasePage.get_element_text(self, userView))

        if userView.is_displayed():
            LoginObject.quit(self)
