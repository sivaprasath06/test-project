import time

from pageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By

from pageObjects.SalesOrderPage import SalesOrderPage
from utilities import ScreenShot


class SalesModulePage(BasePage):
    ORDERS = (By.XPATH, "//a[text()[normalize-space()='Orders']]")
    ORDERS_SUB_MENU = (By.XPATH, "//span[text()='{items}']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_sales_order(self):
        self.click(self.ORDERS)
        orders = list(self.ORDERS_SUB_MENU)
        orders[1] = orders[1].format(items='Orders')
        self.click(tuple(orders))
        ScreenShot.takeScreenshot(self.driver, 'sales_order_page')
        return SalesOrderPage(self.driver)
