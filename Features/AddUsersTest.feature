# Created by TK-LPT-0297 at 8/20/2021
Feature: Add User

  Scenario: Verify that Admin Should be able to Add Users
    Given Admin should be able to login
    Then Admin should be able to navigate to users screen
    Then Admin should be able to click 'Add New Users'
    Then 'Add New Users' form should be displayed
    Then Admin enters first name
    Then Admin enters last name
    Then Admin enters email
    Then Admin selects Field Operator
    Then Admin Enters Hourly Rate
    Then Admin click on Add User
    And User should be added
