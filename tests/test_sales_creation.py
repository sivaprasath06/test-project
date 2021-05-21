import time

import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.SalesModulePage import SalesModulePage
from testData.TestData import TestData
from utilities import ExcelUtil, PropertyFile, ScreenShot
from utilities.BaseClass import BaseClass
from utilities.customLogger import LogGen


class TestSalesModule(BaseClass):
    logger = LogGen.logGen()

    @pytest.mark.order(1)
    def test_sales_module(self, getData):
        driver = self.driver
        # logger = self.getLogger()

        loginpage = LoginPage(driver)

        homepage = loginpage.do_valid_login(TestData.USERNAME, TestData.PASSWORD)
        self.logger.info('Logged In Successfully')

        homepage.click_allapps()
        salesmodulepage = homepage.select_module()
        # homepage.select_module()
        salesorderpage = salesmodulepage.navigate_to_sales_order()

        salesorderpage.click_create_btn()
        salesorderpage.select_customer(getData['customername'])
        salesorderpage.select_validity(getData['validity'])
        salesorderpage.add_product(getData['product1'])
        # salesorderpage.add_product(getData['product2'])
        # salesorderpage.add_product(getData['product3'])
        # salesorderpage.select_quotation(getData['quotation'])
        salesorderpage.select_payment_terms(getData['paymentterms'])
        salesorderpage.click_confirm()
        # salesorderpage.click_create_invoice()
        # salesorderpage.select_down_payment(getData['downpayment'])
        # salesorderpage.click_create_nd_view()
        # salesorderpage.click_validate()
        # salesorderpage.click_register()
        # salesorderpage.click_validate_register()
        # salesorderpage.click_send_print()
        # salesorderpage.click_email_checkbox()
        # salesorderpage.click_print()
        # salesorderpage.click_ok_btn()
        time.sleep(5)
        self.logger.info('Record Created Successfully')

        salesorderpage.open_sales_list()
        salesorderpage.click_on_created_order()
        salesorderpage.click_cancel()
        salesorderpage.click_actions_and_delete()
        self.logger.info('Record Deleted Successfully')

        TestData.write_valid_result()
        homepage.do_logout()
        self.logger.info('Logged Out Successfully')

    @pytest.fixture(params=TestData.getSalesTestData())
    def getData(self, request):
        return request.param
