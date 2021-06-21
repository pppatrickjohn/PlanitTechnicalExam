from selenium import webdriver

class MainMenu:
    link_Home_xpath = "//a[@href='#/home']"
    link_Shop_xpath = "//a[@href='#/shop']"
    link_Contact_xpath = "//a[@href='#/contact']"
    link_Login_xpath = "//*[contains(text(),'Login')]"
    link_Cart_xpath = "//a[@href='#/cart']"

    def __init__(self,driver):
        self.driver = driver

    def goToHome(self,menu):
        self.driver.find_element_by_xpath(self.link_Home_xpath).click()

    def goToShop(self,menu):
        self.driver.find_element_by_xpath(self.link_Shop_xpath).click()

    def goToContact(self,menu):
        self.driver.find_element_by_xpath(self.link_Contact_xpath).click()

    def goToLogin(self,menu):
        self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def goToCart(self,menu):
        self.driver.find_element_by_xpath(self.link_Cart_xpath).click()