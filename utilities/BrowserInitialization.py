from selenium import webdriver


def generateDriver(browser):
    if browser == 'firefox':
        return webdriver.Firefox()
    elif browser == 'chrome':
        return webdriver.Chrome()
    else:
        return webdriver.Edge()
