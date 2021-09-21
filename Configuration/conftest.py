import json
import os

import configparser
import platform

import pytest
from py.path import local
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


def setup():
    # driver = webdriver.Chrome("driver/chromedriver.exe")
    driver = ""
    # headless = context.config.userdata.get("headless", "false").lower()
    headless = "false"
    name = get_config("BROWSER", "browser")
    if get_config("BROWSER", "browser") == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        if headless == "true":
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                  chrome_options=chrome_options)
    elif name == 'firefox':
        if headless == "true":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif name == 'safari':
        if platform.system().lower() != "darwin":
            raise OSError("Safari tests can be run only on MacOS")
        driver = webdriver.Safari(executable_path=os.path.join("usr", "bin", "safaridriver"))
    else:
        raise KeyError('This browser is not supported by this automation script at this time')

    driver.set_page_load_timeout(time_to_wait=100)
    driver.implicitly_wait(15)
    # context.config.setup_logging()
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    yield driver

    driver.quit()


project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def config_data():
    config_file_Path = os.path.join(project_path, "utilities/config.ini")
    config_parser = configparser.RawConfigParser()
    config_parser.read(config_file_Path)
    return config_parser


config = config_data()


def get_config(parent, key):
    return config.get(parent, key)


def set_config(parent, key, value):
    config.set(parent, key, value)
    config_file_Path = os.path.join(project_path, "utilities/config.ini")
    with open(config_file_Path, 'w') as configfile:
        config.write(configfile)
