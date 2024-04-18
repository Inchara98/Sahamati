import configparser
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import webdriver, options

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")


class ReadConfig:

    # @staticmethod
    # def get_chrome_driver_directory():
    #     current_directory = os.path.dirname(__file__)
    #     current_directory = current_directory.replace("Utilities", "")
    #     chrome_directory_path = os.path.join(current_directory, 'driver/chromedriver')
    #     return chrome_directory_path

    # @staticmethod
    # def get_firefox_driver_directory():
    #     current_directory = os.path.dirname(__file__)
    #     current_directory = current_directory.replace("Utilities", "")
    #     firefox_directory_path = os.path.join(current_directory, '/home/inchara/PycharmProjects/Quest/driver'
    #                                                              '/geckodriver')
    #     return firefox_directory_path

    @staticmethod
    def get_application_url():
        url = config.get('common_info', 'baseUrl')
        return url

    @staticmethod
    def getUserID():
        username = config.get('common_info', 'facilitator_username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'facilitator_password')
        return password

    @staticmethod
    def getUser_learner():
        Fakeusername = config.get('common_info', 'learner_username')
        return Fakeusername

    @staticmethod
    def getpassword_learner():
        FakePassword = config.get('common_info', 'learner_password')
        return FakePassword



    @staticmethod
    def get_download_dir():
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd, 'Downloads')
        return download_path

    @staticmethod
    def get_ss_path():
        cwd = os.path.dirname(__file__)
        ss_path = os.path.join(cwd, '../Screenshots/')
        return ss_path

    @staticmethod
    def get_logs_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("Utilities", "")
        logs_directory = os.path.join(current_directory, 'Logs')
        return logs_directory

    @staticmethod
    def get_csv_path():
        csv_path = config.get('common_info', 'csv_path')
        return csv_path
