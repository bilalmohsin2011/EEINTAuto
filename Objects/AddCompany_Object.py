import sys
import time
from Pages.LoginPageFactory import LoginPageFactory
from Utilities.BasePage import BasePage
from Utilities.SetUp import Setup
from Pages.AddCompanyFactory import AddCompanyFactory
from Objects.Login import LoginObject

driver = Setup.driver


class AddCompany:
    def loginAdmin(self):
        LoginObject.openBrowser(self)
        LoginObject.enterUsername(LoginPageFactory.username_Test)
        LoginObject.enterPassword(LoginPageFactory.password_Test)
        LoginObject.clickSubmit(self)

    def navToCompany(self):
        BasePage.wait_for_element_present(self, driver.find_element_by_xpath(AddCompanyFactory.CompanyLink_Xpath), 10)
        usersButton = driver.find_element_by_xpath(AddCompanyFactory.CompanyLink_Xpath)
        usersButton.click()

        time.sleep(3)
        # BasePage.wait_for_element_visible(self, driver.find_element_by_xpath(AddCompanyFactory.displayedCompany), 10)

        if BasePage.is_element_displayed():
            nameOfComapnay = driver.find_element_by_xpath(AddCompanyFactory.displayedCompany)
            print(BasePage.get_element_text(self, nameOfComapnay))
            sys.exit()
        else:
            pass

    def clickAddNewCompany(self):
        BasePage.wait_for_element_visible(self, driver.find_element_by_xpath(AddCompanyFactory.CompanyHeading_Xpath),
                                          10)
        time.sleep(2)
        addCompanyButton = driver.find_element_by_xpath(AddCompanyFactory.addNewCompanyButton_Xpath)
        addCompanyButton.click()

    def addCompanyName(self, companyName):
        BasePage.wait_for_element_visible(self, driver.find_element_by_xpath(AddCompanyFactory.AddCompanyForm_Xpath),
                                          10)
        Name = driver.find_element_by_xpath(AddCompanyFactory.NameField_Xpath)
        Name.send_keys(companyName)
        time.sleep(2)

    def addAddress(self, address):
        CompanyAddress = driver.find_element_by_xpath(AddCompanyFactory.AddressField_Xpath)
        CompanyAddress.send_keys(address)

    def addContactNumber(self, number):
        ContactNumber = driver.find_element_by_xpath(AddCompanyFactory.ContactNumber_Xpath)
        ContactNumber.send_keys(number)

    def addSupervisorFirstName(self, SupervisorFirstName):
        FirstName = driver.find_element_by_xpath(AddCompanyFactory.CsFirstName_Xpath)
        FirstName.send_keys(SupervisorFirstName)

    def addSupervisorLastName(self, SupervisorLastName):
        LastName = driver.find_element_by_xpath(AddCompanyFactory.CsLastName_Xpath)
        LastName.send_keys(SupervisorLastName)

    def addSupervisorEmail(self, SupervisorEmail):
        Email = driver.find_element_by_xpath(AddCompanyFactory.CsEmail_Xpath)
        Email.send_keys(SupervisorEmail)

    def clickClientSupervisor(self):
        addClientSupervisorButton = driver.find_element_by_xpath(AddCompanyFactory.AddCS_Xpath)
        addClientSupervisorButton.click()

    def addedClient(self):
        BasePage.wait_for_element_visible(self, driver.find_element_by_xpath(AddCompanyFactory.supervisorTag_Xpath), 10)
        clientTag = driver.find_element_by_xpath(AddCompanyFactory.supervisorTag_Xpath)

        if clientTag.is_displayed():
            print(BasePage.get_element_text(self, clientTag))

    def clickAddCompany(self):
        clickAdd = driver.find_element_by_xpath(AddCompanyFactory.addCompany)
        clickAdd.click()

    def companyInList(self):
        BasePage.wait_for_element_visible(self, driver.find_element_by_xpath(AddCompanyFactory.displayedCompany), 10)
        companyList = driver.find_element_by_xpath(AddCompanyFactory.displayedCompany)
        if companyList.is_displayed():
            assert True
            LoginObject.quit(self)



