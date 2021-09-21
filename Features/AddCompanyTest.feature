# Created by Bilal Mohsin at 8/26/2021
Feature: Add Company


  Scenario: Admin Should be able to add Company
    Given Admin should be able to login to add company
    Then Admin should be able to navigate to company's screen
    Then Admin should be able to click 'Add New Company'
    Then Admin should be able to add Company Name
    Then Admin should be able to add Address
    Then Admin should be able to add contact
    Then Admin Should be able to add client supervisor first name
    Then Admin should be able to add client supervisor last name
    Then Admin should be able to add client supervisor email
    Then admin should be able to click 'Add Client Supervisor' button
    Then Client Supervisor should be added
    Then Admin should be able to click Add Company
    Then Company should be added in company list