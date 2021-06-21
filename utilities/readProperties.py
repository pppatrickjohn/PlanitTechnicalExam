import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class readConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getExecutionType():
        executionType = config.get('common info','Headless')
        return executionType