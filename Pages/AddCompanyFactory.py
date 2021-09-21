class AddCompanyFactory:
    #   Test Data

    CompanyName = "NetSol"
    Address = "Gulberg, Lahore"
    CsFirstName = "Arshad"
    CsLastName = "Chaiwala"
    CsEmail = "chaiwala@gmail.com"
    ContactNumber = "123456789"

    #   Paths
    CompanyLink_Xpath = "//a[@title='Company']"
    CompanyHeading_Xpath = "//*[text()='Company']"
    addNewCompanyButton_Xpath = "//*[contains(text(), 'add new company')]"
    AddCompanyForm_Xpath = "//h5[text()='Add Company']"
    NameField_Xpath = "//label[text()='Name']//following-sibling::input"
    AddressField_Xpath = "//label[text()='Address']//following-sibling::input"
    ContactNumber_Xpath = "//label[text()='Contact Number']//following-sibling::input"
    CsFirstName_Xpath = "//label[text()='Client Supervisor First Name']//following-sibling::input"
    CsLastName_Xpath = "//label[text()='Client Supervisor Last Name']//following-sibling::input"
    CsEmail_Xpath = "//label[text()='Client Supervisor Email']//following-sibling::input"
    AddCS_Xpath = "//button[text()='Add Client Supervisor']"
    supervisorTag_Xpath = "//span[text()='"+CsEmail+"']"
    addCompany = "//button[text()='Add Company']"
    displayedCompany = "//td//h5[text()='"+CompanyName+"']"
