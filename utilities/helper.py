from utilities import excelUtils

class helperFunctions():
    path = ".//TestData/TestJupiterToys.xlsx"

    def executionDetails(self,testCaseID):
        rows = excelUtils.getRowCount(self.path, 'Test_Execution_Summary')
        list_TestDataToExecute = []
        for x in range(2, rows+1):
            excelTestCaseID = excelUtils.readData(self.path,'Test_Execution_Summary',x,1)
            if testCaseID == excelTestCaseID:
                excelIterationNum = excelUtils.readData(self.path,'Test_Execution_Summary',x,3)
                excelExecuteTestCase = excelUtils.readData(self.path,'Test_Execution_Summary',x,4)
                list_TestDataToExecute.append(str(excelIterationNum))
                list_TestDataToExecute.append(str(excelExecuteTestCase))
                break
        return list_TestDataToExecute

    def contactTestData(self,testCaseID):
        rows1 = excelUtils.getRowCount(self.path, 'Contact_Module')
        list_TestDataToUse = []
        for x in range(3,rows1+1):
            excelTestCaseID1 = excelUtils.readData(self.path,'Contact_Module',x,1)
            if testCaseID == excelTestCaseID1:
                conForeName = excelUtils.readData(self.path,'Contact_Module',x,3)
                conSurName = excelUtils.readData(self.path,'Contact_Module',x,4)
                conEmail = excelUtils.readData(self.path,'Contact_Module',x,5)
                conTelephone = excelUtils.readData(self.path,'Contact_Module',x,6)
                conMsg = excelUtils.readData(self.path,'Contact_Module',x,7)
                conDetails = (str(conForeName) + "," + str(conSurName) + "," + str(conEmail) + "," + str(conTelephone) + "," + str(conMsg))
                list_TestDataToUse.append(conDetails)
        return list_TestDataToUse

    def addToCartTestData(self,testCaseID):
        rows2 = excelUtils.getRowCount(self.path, 'Add_to_Cart_Module')
        list_TestDataToUse = []
        for x in range(3,rows2+1):
            excelTestCaseID2 = excelUtils.readData(self.path,'Add_to_Cart_Module',x,1)
            if testCaseID == excelTestCaseID2:
                itemDetailsToBuy = excelUtils.readData(self.path,'Add_to_Cart_Module',x,3)
                list_TestDataToUse.append(itemDetailsToBuy)
        return list_TestDataToUse