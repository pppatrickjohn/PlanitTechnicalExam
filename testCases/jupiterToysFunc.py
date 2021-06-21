import pytest
from selenium import webdriver
from pageObjects.mainMenu import MainMenu
from pageObjects.contactPage import ContactPage
from pageObjects.shopPage import ShopPage
from pageObjects.cartPage import CartPage
from utilities.readProperties import readConfig
from utilities.customLogger import logGeneration
from utilities.helper import helperFunctions
from utilities import excelUtils
import time

class Test_JupiterToys_Func:
    baseURL = readConfig.getApplicationURL()
    path = ".//TestData/TestJupiterToys.xlsx"

    def test_TC001(self,setup):
        self.toExe = helperFunctions()
        testCaseID = "TC_001"
        executionDetails = self.toExe.executionDetails(testCaseID)
        toExecute = executionDetails[1]
        iterationNum = executionDetails[0]
        list_TestCaseStatus = []

        if str(toExecute) == "YES":
            for i in range(int(iterationNum)):
                self.driver = setup
                self.driver.maximize_window()
                self.driver.get(self.baseURL)
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_jupiterHomepage.png")
                self.menu = MainMenu(self.driver)
                self.menu.goToContact()
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_goToContact.png")
                tc01TD = self.toExe.contactTestData(testCaseID)
                self.conPage = ContactPage(self.driver)
                for j in range(len(tc01TD)):
                    self.conPage.fillContactfields(tc01TD[j])
                    time.sleep(1)
                    if 'None' in tc01TD[j]:
                        self.conPage.clickSubmit()
                        time.sleep(1)
                        if self.conPage.contactFieldsErr():
                            self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_errorValidation.png")
                            list_TestCaseStatus.append("Passed")
                        else:
                            self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_errorValidation.png")
                            list_TestCaseStatus.append("Failed")
                    else:
                        if self.conPage.contactFieldsErr() == "False":
                            self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_noErrorValidation.png")
                            list_TestCaseStatus.append("Passed")

            if "Failed" not in list_TestCaseStatus:
                self.driver.close()
                assert True
            else:
                self.driver.close()
                assert False

    def test_TC002(self,setup):
        self.toExe = helperFunctions()
        testCaseID = "TC_002"
        executionDetails = self.toExe.executionDetails(testCaseID)
        toExecute = executionDetails[1]
        iterationNum = executionDetails[0]
        list_TestCaseStatus = []

        if str(toExecute) == "YES":
            for i in range(int(iterationNum)):
                self.driver = setup
                self.driver.maximize_window()
                self.driver.get(self.baseURL)
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_jupiterHomepage" + str(i+1) +".png")
                self.menu = MainMenu(self.driver)
                self.menu.goToContact()
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_goToContact" + str(i+1) +".png")
                tc02TD = self.toExe.contactTestData(testCaseID)
                self.conPage = ContactPage(self.driver)
                for j in range(len(tc02TD)):
                    self.conPage.fillContactfields(tc02TD[j])
                    self.conPage.clickSubmit()
                    time.sleep(1)
                    if self.conPage.contactSubmitSuccess() == "True":
                        list_TestCaseStatus.append("Passed")
                        self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_SubmitFeedbackSuccess" + str(i+1) +".png")
            if "Failed" not in list_TestCaseStatus:
                self.driver.close()
                assert True
            else:
                self.driver.close()
                assert False

    def test_TC003(self,setup):
        self.toExe = helperFunctions()
        testCaseID = "TC_003"
        executionDetails = self.toExe.executionDetails(testCaseID)
        toExecute = executionDetails[1]
        iterationNum = executionDetails[0]
        list_TestCaseStatus = []

        if str(toExecute) == "YES":
            for i in range(int(iterationNum)):
                self.driver = setup
                self.driver.maximize_window()
                self.driver.get(self.baseURL)
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_jupiterHomepage.png")
                self.menu = MainMenu(self.driver)
                self.menu.goToShop()
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_goToShop.png")
                tc03TD = self.toExe.contactTestData(testCaseID)
                self.conPage = ContactPage(self.driver)
                self.shpPage = ShopPage(self.driver)
                tc03TD = self.toExe.addToCartTestData(testCaseID)
                addedToCartItems = self.shpPage.addToCartVerify(tc03TD)
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_shopSelection.png")

                if addedToCartItems != False:
                    list_TestCaseStatus.append("Passed")
                else:
                    list_TestCaseStatus.append("Failed")
                    self.logger.info(" *************** Cart Quantity is Mismatching with Test Data *************** ")

                self.menu.goToCart()
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_goToCart.png")
                self.cart = CartPage(self.driver)
                cartItemsVerified = self.cart.verifyCartContent(addedToCartItems)
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_cartValidation.png")

                if cartItemsVerified != False:
                    list_TestCaseStatus.append("Passed")
                else:
                    list_TestCaseStatus.append("Failed")

            if "Failed" not in list_TestCaseStatus:
                self.driver.close()
                assert True
            else:
                assert False
                self.driver.close()

    def test_TC004(self,setup):
        self.toExe = helperFunctions()
        testCaseID = "TC_004"
        executionDetails = self.toExe.executionDetails(testCaseID)
        toExecute = executionDetails[1]
        iterationNum = executionDetails[0]
        list_TestCaseStatus = []

        if str(toExecute) == "YES":
            for i in range(int(iterationNum)):
                self.driver = setup
                self.driver.maximize_window()
                self.driver.get(self.baseURL)
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_jupiterHomepage.png")
                self.menu = MainMenu(self.driver)
                self.menu.goToShop()
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_goToShop.png")
                tc04TD = self.toExe.contactTestData(testCaseID)
                self.conPage = ContactPage(self.driver)
                self.shpPage = ShopPage(self.driver)
                tc04TD = self.toExe.addToCartTestData(testCaseID)
                addedToCartItems = self.shpPage.addToCartVerify(tc04TD)
                time.sleep(1)
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_shopSelection.png")

                if addedToCartItems != False:
                    list_TestCaseStatus.append("Passed")
                else:
                    list_TestCaseStatus.append("Failed")

                self.menu.goToCart()
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_goToCart.png")
                self.cart = CartPage(self.driver)
                cartItemsVerified = self.cart.verifyCartContent(addedToCartItems)
                time.sleep(1)
                self.driver.save_screenshot(".\\Screenshots\\" + str(testCaseID) + "_cartValidation.png")

                if cartItemsVerified != False:
                    list_TestCaseStatus.append("Passed")
                else:
                    list_TestCaseStatus.append("Failed")

            if "Failed" not in list_TestCaseStatus:
                self.driver.close()
                assert True
            else:
                assert False
                self.driver.close()