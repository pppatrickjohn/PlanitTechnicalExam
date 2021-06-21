from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def setup():
    options = Options()
    driver = webdriver.Chrome(options=options,
                              executable_path=r"C:\Users\patri\PycharmProjects\Planit_TestAutomationRole_Exam\Driver\chromedriver.exe")
    return driver