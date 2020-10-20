import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path="./TestData/loginData.xlsx"


    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************** Test_002_DDT_Login ***********")
        self.logger.info("***************** Verify Login DDT Test *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in Excel: ", self.rows)

        lst_status=[]  #empty list variable

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** PASSED")
                    self.lp.linkLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** FAILED")
                    self.lp.linkLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** FAILED")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** PASSED")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed...")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed...")
            self.driver.close()
            assert False


        self.logger.info("********** End of Login DDT Test ****************")
        self.logger.info("********** Completed Test_002_DDT_Login ****************")
        #self.driver.close()