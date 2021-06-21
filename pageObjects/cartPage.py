from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class CartPage:
    delay = 3
    table_cartItems_row = "//table[@class='table table-striped cart-items']/tbody[1]/tr"
    table_cartItems_col = "//table[@class='table table-striped cart-items']/tbody[1]/tr[1]/td"
    label_cartSubTotal = "//table[@class='table table-striped cart-items']//following::strong[@class='total ng-binding']"

    def __init__(self,driver):
        self.driver = driver

    def verifyCartContent(self,addedItems):
        list_itemVerificationStatus = []
        list_itemSubTotal = []
        tableRowLen = len(self.driver.find_elements_by_xpath(self.table_cartItems_row))
        tableColLen = len(self.driver.find_elements_by_xpath(self.table_cartItems_col))
        for i in range(tableRowLen):
            itemDetails = addedItems[i].split("-")
            for j in range(1,tableColLen):
                if j == 3:
                    cellValue1 = self.driver.find_element_by_xpath("//table[@class='table table-striped cart-items']/tbody/tr[" + (str(i+1)) + "]/td[" + (str(j)) + "]/input[@type='number']").get_attribute("value")
                    if str(cellValue1) == str(itemDetails[j-1]):
                        list_itemVerificationStatus.append("True")
                    else:
                        list_itemVerificationStatus.append("False")
                elif j == 4:
                    cellValue = self.driver.find_element_by_xpath("//table[@class='table table-striped cart-items']/tbody/tr[" + (str(i+1)) + "]/td[" + (str(j)) + "]").text
                    if str(cellValue) == str(itemDetails[j - 1]):
                        list_itemSubTotal.append(float(str(cellValue).replace("$","")))
                        list_itemVerificationStatus.append("True")
                    else:
                        list_itemVerificationStatus.append("False")
                else:
                    cellValue = self.driver.find_element_by_xpath("//table[@class='table table-striped cart-items']/tbody/tr[" + (str(i+1)) + "]/td[" + (str(j)) + "]").text
                    if str(cellValue) == str(itemDetails[j-1]):
                        list_itemVerificationStatus.append("True")
                    else:
                        list_itemVerificationStatus.append("False")

        uiSubtotalVal = self.driver.find_element_by_xpath(self.label_cartSubTotal).text
        if str(sum(list_itemSubTotal)) == str(uiSubtotalVal.replace("Total: ","")):
            list_itemVerificationStatus.append("True")
        else:
            list_itemVerificationStatus.append("False")

        if "False" not in list_itemVerificationStatus:
            return True
        else:
            return False