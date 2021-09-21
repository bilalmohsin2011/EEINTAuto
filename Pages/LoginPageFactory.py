class LoginPageFactory():

    username_XPATH = "//input[@name='email']"
    password_XPATH = "//input[@type='password']"
    submit_XPATH = "//button[@type='submit']"
    dashboard_Xpath = "//h2[contains(text(),Dashboard)]"

    # Test Data
    username_Test = "info@eeint.com"
    password_Test = "test1234"
