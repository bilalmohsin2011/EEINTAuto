# Created by TK-LPT-0297 at 8/3/2021
Feature: Login OrangeHRMS
  Scenario: Verify that user is able to login
    Given launch chrome browser
    Then Verify that user enters username
    Then Verify user enters password
    And user clicks on submit button