from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class ShopPage:
    delay = 3
    div_product_list = "//div[@class='products ng-scope']"
    btn_ItemtoAdd = "//h4[text()='Stuffed Frog']//following::a[text()='Buy'][1]"
    span_cart_quantity = "//span[@class='cart-count ng-binding']"

    def __init__(self,driver):
        self.driver = driver

    def addToCartVerify(self, itemToAdd):
        WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH, self.div_product_list)))
        cartItems = self.driver.find_element_by_xpath(self.span_cart_quantity).text

        list_AddedItemsTotalPrice = []

        if cartItems == "0":
            cartQty = 0
            if "," not in itemToAdd:
                newItemToAdd = str(itemToAdd) + ","
            else:
                newItemToAdd = itemToAdd

            buyItem = newItemToAdd.split(",")
            for i in range(len(buyItem)):
                itemToBuy = buyItem[i].split("-")
                itemDesc = itemToBuy[0]
                itemQty = itemToBuy[1]
                itemPrice = self.driver.find_element_by_xpath("//h4[text()='" + itemDesc + "']//following::span[@class='product-price ng-binding'][1]").text
                itemTotalPrice = float(itemQty)*float(str(itemPrice).replace("$",""))
                for j in range(int(itemQty)):
                    self.driver.find_element_by_xpath("//h4[text()='" + itemDesc + "']//following::a[text()='Buy'][1]").click()
                    time.sleep(3)
                    cartQty += 1
                list_AddedItemsTotalPrice.append(itemDesc + "-" + itemPrice + "-" + itemQty + "-$" + str(itemTotalPrice))

            newCartItems = self.driver.find_element_by_xpath(self.span_cart_quantity).text

            if str(cartQty) == newCartItems:
                return list_AddedItemsTotalPrice
            else:
                return False