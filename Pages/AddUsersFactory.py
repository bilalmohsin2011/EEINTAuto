class AddUserFactory:
    users_SideMenu_Xpath = "//a[@title='Users']"
    addNewUserButton_Xpath = "//button[@class='btn d-block add-user-btn']"
    fistName_Xpath = "//*[contains(text(),'First Name')]//following-sibling::input"
    lastName_Xpath = "//*[contains(text(),'Last Name')]//following-sibling::input"
    email_Xpath = "//input[@type='email']"
    hourlyRate_Xpath = "//*[contains(text(),'Hourly Rate')]//following-sibling::input"
    AddUserButton_Xpath = "//button[contains(text(),'Add user')]"
    fieldOperator_XPATH = "//label[contains(text(),'Role')]//following-sibling::select"

    Explicit_AddUser_XPATH = "//*[contains(text(),'Add User')]"

    FirstName = "Ricky"
    LastName = "Ponting"
    Email = "bilalmohsin2011@gmail.com"
    HourlyRate = "21"
    role = "Field Operator"

    emailView_XPATH = "//h6[text()='"+Email+"']"
    delete_user = "//*[contains(text(),"+Email+")]/ancestor::td/following-sibling::td[5]//span[2]"
