import os
import sys
import time
import logging
from selenium.webdriver.common.by import By
from Utilities import CustomLogger
from Utilities.readProperties import ReadConfig
from PageObjects.BasePage import Base

sys.path.append(os.getcwd())


class Login(Base):
    username = (By.ID, "username")
    password = (By.ID, "password")
    submit = (By.ID, "kc-login")
    id_name = (
        By.XPATH, "/html/body/app-root/app-dashboard/div/main/app-dashboard-overview/div/table/tbody/tr[1]/td[2]")
    edit_button = (By.XPATH, "/html/body/app-root/app-dashboard/div/main/app-dashboard-overview/div/table/tbody/tr["
                             "1]/td[5]/button[1]")
    auto_id_name = (By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/app-import-entity-dialog/form/div["
                              "2]/mat-form-field/div/div[1]/div[3]/input")
    text_card_value = (By.XPATH, "/html/body/app-root/app-dashboard/div/main/app-dashboard-overview/div/div/div["
                                 "1]/mat-card/mat-card-header/div[2]/mat-card-title")
    column_elements = (By.XPATH, "//tr/td[3]")
    logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/Test_login.log",
                                       level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_login_page(self):
        self.get_url(ReadConfig.get_application_url())
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(self.username).send_keys(ReadConfig.getUserID())
        self.driver.find_element(self.password).send_keys(ReadConfig.getPassword())
        self.click(self.submit)
        time.sleep(5)

    def compare_autofilled_clientid_with_id_name(self):
        text1 = self.get_web_element_text(self.id_name)
        print(text1)
        self.click(self.edit_button)
        text2 = self.get_attribute_value('value', self.auto_id_name)
        print(text2)
        if text1 == text2:
            assert True
            self.logger.info("*********************Test_case_pass*******************************")
        else:
            assert False
        self.logger.info("*********************Test_case_failed*******************************")
        self.logger.info("********************test_autofilled_clientid_name completed*********************")

    def validate_fiu_kpi_value(self):
        text_card_element = self.get_web_element_text(self.text_card_value)
        fiu_number = int(text_card_element.strip())
        column_elements = self.get_web_elements(self.column_elements)
        column_data = [element.text.strip() for element in column_elements]

        # Count the occurrences of 'FIU' in the column data
        count_FIU_in_column = sum('FIU' in item for item in column_data)
        print(fiu_number)
        print(count_FIU_in_column)

        # Compare the count of 'FIU' occurrences with the number displayed in the text card
        if fiu_number == count_FIU_in_column:
            assert True
            print("The number of 'FIU' in the column is equal to the number displayed in the text card.")
        else:
            print("The number of 'FIU' in the column is not equal to the number displayed in the text card.")
            assert False
        self.logger.info("********************test_FIU_kpi_value completed*********************")
