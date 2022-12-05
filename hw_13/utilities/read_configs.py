import configparser
from hw_13.CONSTANTS import ROOT_DIR

abs_path = f'{ROOT_DIR}/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')

    @staticmethod
    def get_email():
        return config.get('user_data', 'email')

    @staticmethod
    def get_password():
        return config.get('user_data', 'password')

    @staticmethod
    def get_invalid_email():
        return config.get('user_data', 'invalid_email')

    @staticmethod
    def get_name():
        return config.get('user_data', 'name')
