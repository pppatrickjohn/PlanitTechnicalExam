import pytest
from selenium import webdriver
from pageObjects.mainMenu import MainMenu
from pageObjects.contactPage import ContactPage
from pageObjects.shopPage import ShopPage
from pageObjects.cartPage import CartPage
import time

class Test_JupiterToys_Func:
    baseURL = "http://jupiter.cloud.planittesting.com"
    noOfIteration = 5
    forename = "asd"
    surname = "asd"
    email = "asd@mail.com"
    telephone = "123"
    message = "test"
    Menu1 = "Contact"
    Menu2 = "Shop"
    Menu3 = "Cart"
    expected = "False"
    itemDetails = "Stuffed Frog-2,Fluffy Bunny-5,Valentine Bear-3"

    def test_populateContact(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        list_TestCaseStatus = []

        self.driver.save_screenshot(".\\Screenshots\\"+"TC01jupiterHomepage.png")
        self.menu = MainMenu(self.driver)
        self.menu.goToContact(self.Menu1)
        self.driver.save_screenshot(".\\Screenshots\\" + "goToContact.png")
        self.conPage = ContactPage(self.driver)
        self.conPage.setForeName(self.forename)
        self.driver.save_screenshot(".\\Screenshots\\" + "contactSetForename.png")
        self.conPage.setSurname(self.surname)
        self.driver.save_screenshot(".\\Screenshots\\" + "contactSetSurname.png")
        self.conPage.setEmail(self.email)
        self.driver.save_screenshot(".\\Screenshots\\" + "contactSetEmail.png")
        self.conPage.setTelephone(self.telephone)
        self.driver.save_screenshot(".\\Screenshots\\" + "contactSetTel.png")
        self.conPage.setMessage(self.message)
        self.driver.save_screenshot(".\\Screenshots\\" + "contactSetMsg.png")
        self.conPage.clickSubmit()

        if self.conPage.contactFieldsErr() == self.expected:
            list_TestCaseStatus.append("Passed")
            if self.conPage.contactSubmitSuccess() == "True":
                time.sleep(1)
                list_TestCaseStatus.append("Passed")
        else:
            list_TestCaseStatus.append("Failed")

        if "Failed" not in list_TestCaseStatus:
            self.driver.close()
            assert True
        else:
            assert False
            self.driver.close()

    def test_addToCart(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        list_TestCaseStatus = []

        self.driver.save_screenshot(".\\Screenshots\\" + "TC02jupiterHomepage.png")
        self.menu = MainMenu(self.driver)
        self.menu.goToShop(self.Menu2)
        self.driver.save_screenshot(".\\Screenshots\\" + "goToShop.png")
        self.shpPage = ShopPage(self.driver)
        addedToCartItems = self.shpPage.addToCartVerify(self.itemDetails)
        self.driver.save_screenshot(".\\Screenshots\\" + "shopSelection.png")

        if addedToCartItems != False:
            list_TestCaseStatus.append("Passed")
        else:
            list_TestCaseStatus.append("Failed")

        self.menu.goToCart(self.Menu3)
        self.driver.save_screenshot(".\\Screenshots\\" + "goToCart.png")
        self.cart = CartPage(self.driver)
        cartItemsVerified = self.cart.verifyCartContent(addedToCartItems)
        self.driver.save_screenshot(".\\Screenshots\\" + "cartValidation.png")

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
