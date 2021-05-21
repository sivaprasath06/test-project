import time

import openpyxl
import os
from utilities import PropertyFile, ExcelUtil
import datetime
from win32com import client

from utilities.PropertyFile import ReadConfig

excel = client.Dispatch(dispatch="Excel.Application")
wb = excel.Workbooks.Add()

today = datetime.date.today()
d1 = today.strftime("%d-%m-%Y")
t = time.localtime()
ctime = time.strftime("%H:%M:%S", t).replace(":", "_")
path = os.path.join(os.getcwd(), f'excel-report\\Test_Data_For_Automating_Sales_Module-{d1}_{ctime}.xlsx')
wb.SaveAs(path)
excel.Application.Quit()

xl = client.Dispatch("Excel.Application")
# xl.Visible = True  # You can remove this line if you don't want the Excel application to be visible
originalFilePath = os.path.join(os.getcwd(), ReadConfig.getExcelFileName())
wb1 = xl.Workbooks.Open(Filename=originalFilePath)

wb2 = xl.Workbooks.Open(Filename=path)

ws1 = wb1.Worksheets(1)
ws1.Copy(Before=wb2.Worksheets(1))

wb2.Close(SaveChanges=True)
xl.Quit()

row = 7


class TestData:
    BASE_URL = ReadConfig.getApplicationURL()
    USERNAME = ReadConfig.getUsername()
    PASSWORD = ReadConfig.getPassword()

    @staticmethod
    def getSalesTestData():
        dataList = []
        filePath = path
        testSheet = ReadConfig.getExcelSheet()

        rowCount = ExcelUtil.get_rowcount(filePath, testSheet)
        for i in range(7, rowCount + 1, 7):  # to get rows
            Dict = {}
            Dict['customername'] = ExcelUtil.read_data(filePath, testSheet, i, 4)
            Dict['validity'] = ExcelUtil.read_data(filePath, testSheet, i + 1, 4)
            Dict['product1'] = ExcelUtil.read_data(filePath, testSheet, i + 2, 4)
            Dict['product2'] = ExcelUtil.read_data(filePath, testSheet, i + 3, 4)
            Dict['product3'] = ExcelUtil.read_data(filePath, testSheet, i + 4, 4)
            Dict['paymentterms'] = ExcelUtil.read_data(filePath, testSheet, i + 5, 4)
            Dict['downpayment'] = ExcelUtil.read_data(filePath, testSheet, i + 6, 4)
            dataList.append(Dict)
        return dataList

    @staticmethod
    def write_valid_result():
        global row
        ExcelUtil.write_data(path,
                             ReadConfig.getExcelSheet(), row, 6,
                             "Record Created Successfully")
        ExcelUtil.write_data(path,
                             ReadConfig.getExcelSheet(), row, 7,
                             'Pass')
        row = row + 7

    @staticmethod
    def write_invalid_result():
        global row
        expected = ExcelUtil.read_data(path,ReadConfig.getExcelSheet(), row, 5)
        if "should not be" in expected:
            expected = expected.replace('should not be', 'is not')
        ExcelUtil.write_data(path,
                             ReadConfig.getExcelSheet(), row, 6,
                             expected)
        ExcelUtil.write_data(path,
                             ReadConfig.getExcelSheet(), row, 7,
                             'Pass')
        row = row + 7
