from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class ContactPage:
    delay = 3
    textbox_forename_xpath = "//input[@name='forename']"
    textbox_surname_xpath = "//input[@name='surname']"
    textbox_email_xpath = "//input[@name='email']"
    textbox_telephone_xpath = "//input[@name='telephone']"
    textarea_message_xpath = "//textarea[@name='message']"
    button_submit_xpath = "//a[@class='btn-contact btn btn-primary']"
    div_mainMsgValidation_xpath = "//div[@class='alert alert-error ng-scope']"
    div_forenameValidation_xpath = "//span[@id='forename-err']"
    div_emailValidation_xpath = "//span[@id='email-err']"
    div_msgValidation_xpath = "//span[@id='message-err']"
    div_contactSubmitSuccess_xpath = "//div[@class='alert alert-success']"
    div_contactSubmitLoading_xpath = "//div[@class='popup modal hide ng-scope' and @aria-hidden='true']"

    def __init__(self,driver):
        self.driver = driver

    def fillContactfields(self, contactTestData):
        conTestData = contactTestData.split(",")
        if 'None' not in conTestData:
            WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH, self.textbox_forename_xpath)))
            self.driver.find_element_by_xpath(self.textbox_forename_xpath).clear()
            self.driver.find_element_by_xpath(self.textbox_forename_xpath).send_keys(conTestData[0])
            self.driver.find_element_by_xpath(self.textbox_surname_xpath).clear()
            self.driver.find_element_by_xpath(self.textbox_surname_xpath).send_keys(conTestData[1])
            self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
            self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(conTestData[2])
            self.driver.find_element_by_xpath(self.textbox_telephone_xpath).clear()
            self.driver.find_element_by_xpath(self.textbox_telephone_xpath).send_keys(conTestData[3])
            self.driver.find_element_by_xpath(self.textarea_message_xpath).clear()
            self.driver.find_element_by_xpath(self.textarea_message_xpath).send_keys(conTestData[4])
#        self.clickSubmit()
        time.sleep(1)

    def contactFieldsErr(self):
        if len(self.driver.find_elements(By.XPATH, self.div_mainMsgValidation_xpath)) > 0:
            if len(self.driver.find_elements(By.XPATH, self.div_forenameValidation_xpath)) > 0 or len(self.driver.find_elements(By.XPATH, self.div_emailValidation_xpath)) > 0 or len(self.driver.find_elements(By.XPATH, self.div_msgValidation_xpath)) > 0:
                return "True"
        else:
            return "False"

    def clickSubmit(self):
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()

    def contactSubmitSuccess(self):
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH,self.div_contactSubmitSuccess_xpath)))
        if not self.driver.find_element_by_xpath(self.div_contactSubmitSuccess_xpath):
            return "False"
        else:
            return "True"