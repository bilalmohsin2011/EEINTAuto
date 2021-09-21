from behave import *
from self import self
from Pages.AddCompanyFactory import AddCompanyFactory

from Objects.AddCompany_Object import AddCompany

use_step_matcher("re")


class AddCompanySteps:
    @given("Admin should be able to login to add company")
    def login(context):
        AddCompany.loginAdmin(self)

    @then("Admin should be able to navigate to company's screen")
    def navToCompany(context):
        AddCompany.navToCompany(self)
        AddCompany.companyInList(self)

    @then("Admin should be able to click 'Add New Company'")
    def clickNewCompany(context):
        AddCompany.clickAddNewCompany(self)

    @then("Admin should be able to add Company Name")
    def addName(context):
        AddCompany.addCompanyName(self, AddCompanyFactory.CompanyName)

    @then("Admin should be able to add Address")
    def addAddress(context):
        AddCompany.addAddress(self, AddCompanyFactory.Address)

    @then("Admin Should be able to add client supervisor first name")
    def SuperVisorFirstName(context):
        AddCompany.addSupervisorFirstName(self, AddCompanyFactory.CsFirstName)

    @then("Admin should be able to add client supervisor last name")
    def SuperVisorLastName(context):
        AddCompany.addSupervisorLastName(self, AddCompanyFactory.CsLastName)

    @then("Admin should be able to add contact")
    def addContact(context):
        AddCompany.addContactNumber(self, AddCompanyFactory.ContactNumber)


    @then("Admin should be able to add client supervisor email")
    def SupervisorEmail(context):
        AddCompany.addSupervisorEmail(self, AddCompanyFactory.CsEmail)

    @then("admin should be able to click 'Add Client Supervisor' button")
    def clickAddSupervisor(context):
        AddCompany.clickClientSupervisor(self)

    @then("Client Supervisor should be added")
    def supervisorIsAdded(context):
        AddCompany.addedClient(self)

    @then("Admin should be able to click Add Company")
    def clickToAddCompany(context):
        AddCompany.clickAddCompany(self)


    @then("Company should be added in company list")
    def companyAddedInList(context):
        AddCompany.companyInList(self)


