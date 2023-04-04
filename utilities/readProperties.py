from configparser import ConfigParser

config = ConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        # url = config.get('common info','baseURL')
        url = config['common info']['baseURL']
        return url

    @staticmethod
    def getUseremail():
        username = config['common info']['username']
        return username

    @staticmethod
    def getPassword():
        password = config['common info']['password']
        return password
