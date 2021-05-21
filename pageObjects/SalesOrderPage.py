import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from pageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By

from utilities import ScreenShot

orderNumber = ''


class SalesOrderPage(BasePage):
    CREATE_BTN = (By.XPATH, "//button[@accesskey='c']")
    TITLE = (By.XPATH, "//div[@class='oe_title']//span[1]")
    SALE_ORDER_PAGE = (By.XPATH, "(//li[@class='breadcrumb-item']//a)[1]")
    SALES_LIST = (By.XPATH, "//table[contains(@class,'o_list_view table')]/tbody[1]/tr")
    CUSTOMERFIELD = (By.XPATH, "(//div[@class='o_input_dropdown']//input)[1]")
    SEARCHMORE = (By.XPATH, "(//li[@class='o_m2o_dropdown_option ui-menu-item']//a)[1]")
    SELECTCUSTOMER = (By.XPATH, "(//tr[@class='o_data_row'])")
    VALIDITY = (By.XPATH, "(//input[@name='validity_date'])[1]")
    DATE_PICKER = (By.XPATH, "//div[@class='datepicker']//div")
    QUOTATION_TEMPLATE = (By.XPATH, "(//label[text()='Quotation Template']/following::input)[1]")
    ADD_PRODUCT = (By.XPATH, "//td[@colspan='7']//a[1]")
    PRODUCT_INPUT = (By.XPATH, "(//input[@class='o_input ui-autocomplete-input'])[7]")
    QUOTATION = (By.LINK_TEXT, "{quotation}")
    PAYMENT_TERMS = (By.XPATH, "(//label[text()='Payment Terms']/following::input)[1]")
    PAYMENT = (By.LINK_TEXT, "{payment}")
    OPTIONS = (By.XPATH, "(//input[@type='radio'])[3]")
    DOWN_PAYMENT = (By.XPATH, "(//label[text()='Down Payment Amount']/following::input)[1]")
    CONFIRM_BTN = (By.XPATH, "(//button[@name='action_confirm'])[2]")
    CREATE_INVOICE = (By.XPATH, "//button[@class='btn btn-primary']//span[1]")
    CREATE_VIEW = (By.XPATH, "(//button[@name='create_invoices']//span)[1]")
    VALIDATE = (By.XPATH, "//button[@name='action_invoice_open']//span[1]")
    REGISTER = (By.XPATH, "(//div[@class='o_statusbar_buttons']//button)[3]")
    VALIDATE_REGISTER = (By.XPATH, "(//button[@class='btn btn-primary']//span)[3]")
    SEND_PRINT = (By.XPATH, "//div[@class='o_statusbar_buttons']//button[1]")
    PRINT_BTN = (By.XPATH, "(//button[@name='send_and_print_action'])[3]")
    CANCEL_BTN = (By.NAME, "action_cancel")
    ACTIONS = (By.XPATH, "//button[text()[normalize-space()='Action']]")
    ACTION_MENU = (By.XPATH, "//div[@class='btn-group']//div[2]//div//child::a")
    DIALOG_OK = (By.XPATH, "(//div[@class='modal-dialog']//div//footer//button)[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_actions_and_delete(self):
        time.sleep(2)
        self.click(self.ACTIONS)
        actionMenuList = self.driver.find_elements(*self.ACTION_MENU)
        for ele1 in actionMenuList:
            if ele1.text == "Delete":
                ele1.click()
                break
        self.click(self.DIALOG_OK)

    def click_cancel(self):
        self.click(self.CANCEL_BTN)

    def click_on_created_order(self):
        salesList = self.driver.find_elements(*self.SALES_LIST)
        for ele1 in salesList:
            ele2 = ele1.find_elements_by_xpath("./child::*")[1]
            if ele2.text == orderNumber:
                ele2.click()
                break

    def open_sales_list(self):
        self.click(self.SALE_ORDER_PAGE)

    def add_product(self, value):
        time.sleep(2)
        self.click(self.ADD_PRODUCT)
        time.sleep(2)
        input = self.driver.find_element(*self.PRODUCT_INPUT)
        input.send_keys(value)
        time.sleep(2)
        input.send_keys(Keys.ENTER)
        time.sleep(2)
        input.send_keys(Keys.ENTER)
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB * 5)
        actions.perform()

    def select_validity(self, value):
        time.sleep(3)
        self.click(self.VALIDITY)
        self.datepicker(self.DATE_PICKER, value)

    def click_create_btn(self):
        self.click(self.CREATE_BTN)

    def select_customer(self, value):
        self.click(self.CUSTOMERFIELD)
        self.click(self.SEARCHMORE)
        time.sleep(1)
        customerTrList = self.driver.find_elements(*self.SELECTCUSTOMER)
        for ele1 in customerTrList:
            ele2 = ele1.find_elements_by_xpath("./child::*")[0]
            if ele2.text == value:
                ele2.click()
                break

        time.sleep(3)

    def select_quotation(self, value):
        self.click(self.QUOTATION_TEMPLATE)
        quotationLocator = list(self.QUOTATION)
        quotationLocator[1] = quotationLocator[1].format(quotation=value)
        self.click(tuple(quotationLocator))

    def select_payment_terms(self, value):
        self.click(self.PAYMENT_TERMS)
        paymentLocator = list(self.PAYMENT)
        paymentLocator[1] = paymentLocator[1].format(payment=value)
        self.click(tuple(paymentLocator))

    def select_down_payment(self, value):
        time.sleep(3)
        pyautogui.click(611, 351, 1)
        self.clearAndType(self.DOWN_PAYMENT, value)

    def click_confirm(self):
        global orderNumber
        self.click(self.CONFIRM_BTN)
        time.sleep(3)
        orderNumber = self.getText(self.TITLE)
        ScreenShot.takeScreenshot(self.driver, 'order_created')

    def click_create_invoice(self):
        time.sleep(2)
        self.click(self.CREATE_INVOICE)
        time.sleep(2)
        ScreenShot.takeScreenshot(self.driver, 'create_invoice')

    def click_create_nd_view(self):
        self.click(self.CREATE_VIEW)

    def click_validate(self):
        self.click(self.VALIDATE)

    def click_register(self):
        self.click(self.REGISTER)
        ScreenShot.takeScreenshot(self.driver, 'register_payment')

    def click_validate_register(self):
        self.click(self.VALIDATE_REGISTER)

    def click_send_print(self):
        time.sleep(2)
        self.click(self.SEND_PRINT)

    def click_email_checkbox(self):
        time.sleep(6)
        pyautogui.click(376, 293, 1)

    def click_print(self):
        self.click(self.PRINT_BTN)
        ScreenShot.takeScreenshot(self.driver, 'invoice_generated')

    def click_ok_btn(self):
        time.sleep(6)
        pyautogui.click(1060, 679, 1)
