from jproperties import Properties

conf = Properties()

with open('conf.properties', 'rb') as read_prop:
    conf.load(read_prop)


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = conf.get('url').data
        return url

    @staticmethod
    def getUsername():
        username = conf.get('username').data
        return username

    @staticmethod
    def getPassword():
        password = conf.get('password').data
        return password

    @staticmethod
    def getExcelFileName():
        fileName = conf.get('excelFilePath').data
        return fileName

    @staticmethod
    def getExcelSheet():
        sheetName = conf.get('salestd').data
        return sheetName

    @staticmethod
    def getModuleName():
        moduleName = conf.get('module_name').data
        return moduleName
