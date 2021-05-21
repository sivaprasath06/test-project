import time

from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.HomePage import HomePage
from utilities import ScreenShot, ExcelUtil, PropertyFile


class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGINBTN = (By.XPATH, "//button[contains(@class,'btn btn-primary')]")
    ALERT = (By.XPATH, "//p[@class='alert alert-danger']")

    def __init__(self, driver):
        super().__init__(driver)

    def do_valid_login(self, username, password):
        self.clearAndType(self.USERNAME, username)
        self.clearAndType(self.PASSWORD, password)
        ScreenShot.takeScreenshot(self.driver, 'credentials_filled')
        self.click(self.LOGINBTN)
        time.sleep(3)
        assert "Odoo" != self.driver.title
        ScreenShot.takeScreenshot(self.driver, 'successfully_logged_in')
        return HomePage(self.driver)
