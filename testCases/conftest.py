from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.readProperties import readConfig
import pytest

@pytest.fixture()
def setup():
    options = Options()
    options.headless = readConfig.getExecutionType()
    driver = webdriver.Chrome(options=options,
                              executable_path=r"C:\Users\patri\PycharmProjects\Planit_TestAutomationRole_Exam\Driver\chromedriver.exe")
    return driver

########## Pytest HTML Report ##########
#hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Plant Test Automation Role Exam'
    config._metadata['Module Name'] = 'Jupiter Toys Shop'
    config._metadata['Tester'] = 'Patrick John Bawalan'

#hook for delete/modify environment info in HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)