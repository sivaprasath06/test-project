import allure
from allure_commons.types import AttachmentType


def takeScreenshot(driver, name):
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
