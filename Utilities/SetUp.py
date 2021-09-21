from selenium import webdriver


class Setup:
    driver = webdriver.Chrome("Drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(20)
    url = "http://eeint-dev-demo.herokuapp.com/"
    driver.get(url)