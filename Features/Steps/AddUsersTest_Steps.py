from pytest_bdd import *
from behave import given, when, then, step
from Objects.AddUsers_Object import AddUsers
import time
import self as self
from Utilities.SetUp import Setup
from Objects.Login import LoginObject


class Add_Users:

    @given("Admin should be able to login")
    def login(context):
        AddUsers.login(self)

    @then("Admin should be able to navigate to users screen")
    def Go_To_Users_Screen(context):
        AddUsers.goToUsersScreen(self)

    @then("Admin should be able to click 'Add New Users'")
    def click_addNewUser(context):
        # time.sleep(5)
        AddUsers.clickAddNewUsers(self)

    @then("'Add New Users' form should be displayed")
    def formDisplayed(context):
        AddUsers.openAddUserForm(self)

    @then("Admin enters first name")
    def typeFirstName(context):
        AddUsers.enterFirstName(self)

    @then("Admin enters last name")
    def typeLastName(context):
        AddUsers.enterLastName(self)

    @then("Admin enters email")
    def typeEmail(context):
        AddUsers.enterEmail(self)

    @then("Admin selects Field Operator")
    def selectFieldOpertaor(context):
        AddUsers.chooseFieldOperator(self)

    @then("Admin Enters Hourly Rate")
    def enterHourlyRate(context):
        AddUsers.enterHourlyRate(self)

    @then("Admin click on Add User")
    def submitAddUser(context):
        AddUsers.submitUser(self)

    @then("User should be added")
    def verifyViewUser(context):
        time.sleep(2)
        AddUsers.userDisplayed(self)


