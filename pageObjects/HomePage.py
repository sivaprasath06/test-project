from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.SalesModulePage import SalesModulePage
from utilities import ScreenShot
from utilities.PropertyFile import ReadConfig


class HomePage(BasePage):
    USERMENU = (By.XPATH, "(//li[@class='o_user_menu']//a)[1]")
    LOGOUTBTN = (By.XPATH, "//a[@data-menu='logout']")
    ALLAPPS = (By.XPATH, "(//a[@data-toggle='dropdown'])[1]")
    HEADING = (By.XPATH, "(//a[@role='button'])[1]")
    MODULE = (By.XPATH, "//a[text()[normalize-space()='{module}']]")

    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        self.click(self.USERMENU)
        self.click(self.LOGOUTBTN)

    def click_allapps(self):
        self.click(self.ALLAPPS)

    def select_module(self):
        module = list(self.MODULE)
        module[1] = module[1].format(module=ReadConfig.getModuleName())
        self.click(tuple(module))

        assert True == self.check_text_presence(self.HEADING, 'Sales')
        ScreenShot.takeScreenshot(self.driver, 'opened_sales_app')
        return SalesModulePage(self.driver)
