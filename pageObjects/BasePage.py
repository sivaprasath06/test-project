import time

from utilities import CustomWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        time.sleep(1)
        CustomWait.wait(self.driver, 'click', by_locator).click()
        time.sleep(1)

    def presenceOfElement(self, by_locator):
        return CustomWait.wait(self.driver, 'presence', by_locator)

    def clearAndType(self, by_locator, value, keyPress=None):
        time.sleep(1)
        ele = CustomWait.wait(self.driver, 'presence', by_locator)
        ele.clear()
        if keyPress is None:
            ele.send_keys(value)
        else:
            ele.send_keys(value, keyPress)

    def type(self, by_locator, value, keyPress=None):
        time.sleep(1)
        ele = CustomWait.wait(self.driver, 'presence', by_locator)
        if keyPress is None:
            ele.send_keys(value)
        else:
            ele.send_keys(value, keyPress)
        time.sleep(1)

    def getText(self, by_locator):
        time.sleep(1)
        ele = CustomWait.wait(self.driver, 'presence', by_locator)
        time.sleep(1)
        return ele.text

    def check_text_presence(self, by_locator, text):
        ele = CustomWait.wait(self.driver, 'text', by_locator, text)
        return ele

    def datepicker(self, by_locator, value):
        date = value.strftime('%m/%d/%Y').split('/')
        m = int(date[0])
        d = int(date[1])
        y = int(date[2])

        datepickerList = self.driver.find_elements(*by_locator)

        dateTable = datepickerList[0].find_elements_by_xpath("./child::*")
        dateTableList = dateTable[0].find_elements_by_xpath("./child::*")
        dateThead = dateTableList[0]
        dateTbody = dateTableList[1]
        datePrev = dateThead.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[0]
        dateCenter = dateThead.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[1]
        dateNext = dateThead.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[2]

        monthTable = datepickerList[1].find_elements_by_xpath("./child::*")
        monthTableList = monthTable[0].find_elements_by_xpath("./child::*")
        monthThead = monthTableList[0]
        monthTbody = monthTableList[1]
        monthPrev = monthThead.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[0]
        monthCenter = monthThead.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[1]
        monthNext = monthThead.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[2]

        yearTable = datepickerList[2].find_elements_by_xpath("./child::*")
        yearTableList = yearTable[0].find_elements_by_xpath("./child::*")
        yearThead = yearTableList[0]
        yearTbody = yearTableList[1]
        yearPrev = yearThead.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[0]
        yearCenter = yearThead.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[1]
        yearNext = yearThead.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[2]

        dateCenter.click()
        monthCenter.click()

        while True:
            fromY = int(yearCenter.text.split('-')[0]) - 1
            toY = int(yearCenter.text.split('-')[1]) + 1
            if fromY <= y <= toY:
                currentYear = yearTbody.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[
                    0].find_elements_by_xpath("./child::*")
                for ele in currentYear:
                    if int(ele.text) == y:
                        ele.click()
                        break
                currentMonth = monthTbody.find_elements_by_xpath("./child::*")[0].find_elements_by_xpath("./child::*")[
                    0].find_elements_by_xpath("./child::*")
                currentMonth[m - 1].click()
                week = dateTbody.find_elements_by_xpath("./child::*")
                # currentDate = week.find_elements_by_xpath("./child::*")
                status = False
                for ele1 in week:
                    for ele2 in ele1.find_elements_by_xpath("./child::*"):
                        if ele2.get_attribute('data-day') is not None:
                            temp = ele2.get_attribute('data-day').split('/')
                            if int(temp[0]) == m:
                                if int(temp[1]) == d:
                                    ele2.click()
                                    status = True
                                    break
                    if status:
                        break
                break
                # click on the month and date inside
            if y < fromY:
                yearPrev.click()
            if y > toY:
                yearNext.click()
