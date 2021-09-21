import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('common-info', 'baseURL')
        return url
