import os
import sys
import time
import logging

from selenium.common import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from Utilities import CustomLogger
from Utilities.readProperties import ReadConfig
from PageObjects.BasePage import Base

sys.path.append(os.getcwd())


class AAcommons(Base):
    username = "username"
    password = "password"
    submit = (By.ID, "kc-login")
    column_elements = (By.XPATH, "//tr/td[3]")
    edit_button = (By.XPATH, "/html/body/app-root/app-dashboard/div/main/app-dashboard-overview/div/table/tbody/tr["
                             "1]/td[5]/button[1]")
    text_field = (By.XPATH, "//app-import-entity-dialog/form/div["
                            "2]/mat-form-field/div/div[1]/div[3]/input")
    text_field1 = ("//app-import-entity-dialog/form/div["
                   "2]/mat-form-field/div/div[1]/div[3]/input")
    secret_key_field = "//app-import-entity-dialog/form/div[3]/mat-form-field/div/div[1]/div[3]/input"
    secret_key_field1 = (By.XPATH, "//app-import-entity-dialog/form/div[3]/mat-form-field/div/div[1]/div[3]/input")
    submit_button = (By.XPATH, "//app-import-entity-dialog/form/button")
    alert_message = "/html/body/div[4]/div/div/div"
    modified_successfully_alert_message = "//div[@aria-label='Modified Successfully']"
    alert_messages_list = (By.XPATH, "//div[@aria-label='client Id and secret Does not match.']")
    id_name = (By.XPATH, "//app-dashboard-overview/div/table/tbody/tr[1]/td[2]")
    auto_id_name = (By.XPATH, "//app-import-entity-dialog/form/div[2]/mat-form-field/div/div[1]/div[3]/input")
    cannot_find_your_entity = (By.XPATH, "//app-dashboard-overview/div/form/div/div[4]/button")
    details_page_submit_button = ("/html/body/app-root/app-dashboard/div/main/app-dashboard-entity"
                                  "-component/app-entity/div/div/div[2]/form/div/button")
    client_id_fiel1 = (By.XPATH, "//app-import-entity-dialog/form/div[2]/mat-form-field/div/div[1]/div[3]/input")
    client_id_field = "//app-import-entity-dialog/form/div[2]/mat-form-field/div/div[1]/div[3]/input"
    back_button = (By.XPATH, "//app-dashboard-entity-component/app-entity/div/div/div[2]/div/a")
    certificate_text_field1 = ("//app-dashboard-entity-component/app-entity/div/div/div[2]/form/mat-form-field["
                               "4]/div/div[1]/div/textarea")
    certificate_text_field = (By.XPATH, "//app-dashboard-entity-component/app-entity/div/div/div[2]"
                                        "/form/mat-form-field[4]/div/div[1]/div/textarea")
    base_url_field = (By.XPATH, "//app-entity/div/div/div[2]/form/mat-form-field[6]/div/div[1]/div/input")
    base_url_field1 = "//app-entity/div/div/div[2]/form/mat-form-field[6]/div/div[1]/div/input"
    entity_info_name = (By.XPATH, "//app-entity/div/div/div[2]/form/mat-form-field[1]/div/div[1]/div/input")
    entity_info_name1 = "//app-entity/div/div/div[2]/form/mat-form-field[1]/div/div[1]/div/input"
    entity_info_id = (By.XPATH, "//app-entity/div/div/div[2]/form/mat-form-field[2]/div/div[1]/div/input")
    entity_info_id1 = "//app-entity/div/div/div[2]/form/mat-form-field[2]/div/div[1]/div/input"
    entity_info_code = (By.XPATH, "//app-entity/div/div/div[2]/form/mat-form-field[3]/div/div[1]/div/input")
    entity_info_code1 = "//app-entity/div/div/div[2]/form/mat-form-field[3]/div/div[1]/div/input"
    entity_handle = (By.XPATH, "//app-entity/div/div/div[2]/form/mat-form-field[5]/div/div[1]/div/input")
    entity_handle1 = "//app-entity/div/div/div[2]/form/mat-form-field[5]/div/div[1]/div/input"
    web_view_url = (By.XPATH, "//app-entity/div/div/div[2]/form/mat-form-field[7]/div/div[1]/div/input")
    web_view_url1 = "//app-entity/div/div/div[2]/form/mat-form-field[7]/div/div[1]/div/input"
    regulated_name = (By.XPATH, "//app-entity/div/div/div[2]/form/mat-form-field[8]/div/div[1]/div/input")
    regulated_name1 = "//app-entity/div/div/div[2]/form/mat-form-field[8]/div/div[1]/div/input"
    category_field = (By.XPATH, "//app-entity/div/div/div[2]/form/mat-form-field[9]/div/div[1]/div/input")
    category_field1 = "//app-entity/div/div/div[2]/form/mat-form-field[9]/div/div[1]/div/input"
    licence_type = (By.XPATH, "//app-entity/div/div/div[2]/form/mat-form-field[10]/div/div[1]/div/input")
    licence_type1 = "//app-entity/div/div/div[2]/form/mat-form-field[10]/div/div[1]/div/input"
    ips_field = (By.XPATH, "//app-entity/div/div/div[2]/form/div[1]/mat-form-field/div/div["
                           "1]/div/mat-chip-list/div/input")
    ips_field1 = "//app-entity/div/div/div[2]/form/div[1]/mat-form-field/div/div[1]/div/mat-chip-list/div/input"
    add_field_dropdown = "//app-entity/div/div/div[2]/form/mat-form-field[12]/div/div[1]/div/mat-select"
    ip_checkbox = (By.XPATH, "//html/body/div[3]/div[2]/div/div/div/mat-option[1]/span")
    yes_button = (By.XPATH, "//html/body/div[3]/div[4]/div/mat-dialog-container/app-confirm-dialog"
                            "/div[2]/button[2]")
    inbound_checkbox = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/mat-option[2]/span")
    inbound_field = (By.XPATH, "//app-entity/div/div/div[2]/form/div[2]/mat-form-field/div/div["
                               "1]/div/mat-chip-list/div/input")
    inbound_field1 = "//app-entity/div/div/div[2]/form/div[2]/mat-form-field/div/div[1]/div/mat-chip-list/div/input"
    outbound_checkbox = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/mat-option[3]/span")
    outbound_field1 = "//app-entity/div/div/div[2]/form/div[3]/mat-form-field/div/div[1]/div/mat-chip-list/div/input"
    outbound_field = (By.XPATH, "//app-entity/div/div/div[2]/form/div[3]/mat-form-field/div/div["
                                "1]/div/mat-chip-list/div/input")

    logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/Test_login.log",
                                       level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_login_page(self):
        time.sleep(3)
        self.get_url(ReadConfig.get_application_url())
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(By.ID, self.username).send_keys(ReadConfig.getUserID())
        self.driver.find_element(By.ID, self.password).send_keys(ReadConfig.getPassword())
        self.click(self.submit)
        time.sleep(5)

    def check_column_entry(self):
        column_elements = self.get_web_elements(self.column_elements)
        # Check if the column is not null and has values
        if column_elements:
            assert True
            self.logger.info("Expected behavior: Column is not null and has values.")
        else:
            self.logger.info("Unexpected behavior: Column is null or doesn't have values.")
            assert False

    def click_edit_button(self):
        self.click(self.edit_button)

    def get_text_field_value(self):
        # Get the value of the text field
        field_value = self.get_attribute_value('value', self.text_field)

        # Check if the value is present and not empty
        if field_value is not None and field_value.strip() != '':
            assert True
            print("Value is present in the text field and it is not empty.")
        else:
            print("Value is not present in the text field or it is empty.")
            assert False

    def check_text_fill_is_editable(self):
        initial_value = self.get_attribute_value('value', self.text_field)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.text_field1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.text_field)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value == initial_value:
            print("Text field is not editable.")
            assert True
        else:
            print("Text field is editable.")
            assert False

    def enter_correct_secret_key(self):
        self.driver.find_element(By.XPATH, self.secret_key_field).send_keys('dOSuQA3TUeYeDUFstYsAZcj6TfgQjjBg')

    def enter_wrong_secret_key(self):
        self.driver.find_element(By.XPATH, self.secret_key_field).send_keys('12345')

    def check_alert_message(self):
        time.sleep(5)
        self.enter_wrong_secret_key()
        self.click(self.submit_button)
        time.sleep(5)

        # Check if the error message element is present
        try:
            error_message = self.driver.find_element(By.XPATH, self.alert_message)
            if error_message.text.strip() != '':
                print("Error message:", error_message.text)
                print("Error message element is present and not null.")
            else:
                print("Error message element is present but null.")
        except NoSuchElementException:
            print("No error message element present.")

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

    def count_error_message(self):
        def count_error_messages():
            try:
                # Locate all error message elements
                # error_messages = self.driver.find_elements(By.XPATH, "//div[@aria-label='client Id and secret Does "
                #                                                      "not match.']")
                error_messages = self.get_web_elements(self.alert_messages_list)
                return len(error_messages)
            except:
                return 0

        # Click the submit button multiple times
        for _ in range(8):  # Change 5 to the desired number of times you want to click
            # Find and click the submit button
            self.click(self.submit_button)
            time.sleep(1)
            # time.sleep(1)  # Add a short delay to allow the page to update

        # Count the number of error messages displayed
        error_message_count = count_error_messages()

        # Check if multiple error messages are not displayed
        if error_message_count <= 1:
            assert True
            self.logger.info("Expected behavior: Error message is displayed at most once.")
        else:
            self.logger.error("Unexpected behavior: Multiple error messages are displayed.")
            assert False

    def click_cannot_find_your_entity(self):
        self.click(self.cannot_find_your_entity)

    def check_secret_text_fill_is_editable(self):
        initial_value = self.get_attribute_value('value', self.secret_key_field1)
        print(initial_value)

        self.enter_correct_secret_key()

        current_value = self.get_attribute_value('value', self.secret_key_field1)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value != initial_value:
            print("Secret key text field is editable.")
            assert True
        else:
            print("Text field is not editable.")
            assert False

    def click_submit_button(self):
        self.click(self.submit_button)

    def click_submit_button2(self):
        self.click(self.details_page_submit_button)

    def check_modified_suucessfull_alert_message(self):
        element = self.driver.find_element(By.XPATH, self.details_page_submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)
        element.click()
        time.sleep(4)
        # Check if the error message element is present
        try:
            error_message = self.driver.find_element(By.XPATH, self.modified_successfully_alert_message)
            if error_message.text.strip() != '':
                print("Error message:", error_message.text)
                print("Error message element is present and not null.")
                assert True
            else:
                print("Error message element is present but null.")
                assert False
        except NoSuchElementException:
            print("No error message element present.")
            assert False

    def enter_client_id(self):
        self.driver.find_element(By.XPATH, self.client_id_field).send_keys('enter_client_id')

    def check_client_id_text_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.client_id_fiel1)
        print(initial_value)

        self.enter_client_id()

        current_value = self.get_attribute_value('value', self.client_id_fiel1)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value != initial_value:
            print("client_id text field is editable.")
            assert True
        else:
            print("client_id text field is not editable.")
            assert False

    def check_secret_key_text_field_is_editable_CFE(self):
        initial_value = self.get_attribute_value('value', self.client_id_fiel1)
        print(initial_value)

        self.enter_client_id()

        current_value = self.get_attribute_value('value', self.client_id_fiel1)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value != initial_value:
            print("client_id text field is editable.")
            assert True
        else:
            print("client_id text field is not editable.")
            assert False

    def click_back_button(self):
        self.click(self.back_button)

    def open_details_page(self):
        self.open_login_page()
        self.click_edit_button()
        self.enter_correct_secret_key()
        self.click_submit_button()

    def check_certificate_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.certificate_text_field)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.certificate_text_field1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.certificate_text_field)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value != initial_value:
            print("Certificate Text field is  editable.")
            assert True
        else:
            print("Text field is not editable.")
            assert False

    def check_base_url_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.base_url_field)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.base_url_field1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.base_url_field)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value != initial_value:
            print("base url Text field is  editable.")
            assert True
        else:
            print("base url field is not editable.")
            assert False

    def check_entity_info_name_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.entity_info_name)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.entity_info_name1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.entity_info_name)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value == initial_value:
            print("entity name Text field is not editable.")
            assert True
        else:
            print("entity name Text field is editable.")
            assert False

    def check_entity_info_id_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.entity_info_id)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.entity_info_id1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.entity_info_id)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value == initial_value:
            print("entity id Text field is not editable.")
            assert True
        else:
            print("entity id Text field is editable.")
            assert False

    def check_entity_info_code_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.entity_info_code)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.entity_info_code1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.entity_info_code)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value == initial_value:
            print("entity code Text field is not editable.")
            assert True
        else:
            print("entity code Text field is editable.")
            assert False

    def check_entity_handle_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.entity_handle)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.entity_handle1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.entity_handle)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value == initial_value:
            print("entity handle Text field is not editable.")
            assert True
        else:
            print("entity handle Text field is editable.")
            assert False

    def check_web_view_url_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.web_view_url)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.web_view_url1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.web_view_url)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value == initial_value:
            print("entity web view url Text field is not editable.")
            assert True
        else:
            print("entity web view url Text field is editable.")
            assert False

    def check_regulated_name_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.regulated_name)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.regulated_name1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.regulated_name)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value == initial_value:
            print("regulated name Text field is not editable.")
            assert True
        else:
            print("regulated name Text field is editable.")
            assert False

    def check_category_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.category_field)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.category_field1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.category_field)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value == initial_value:
            print("category Text field is not editable.")
            assert True
        else:
            print("category Text field is editable.")
            assert False

    def check_licence_field_is_editable(self):
        initial_value = self.get_attribute_value('value', self.licence_type)
        print(initial_value)

        self.driver.find_element(By.XPATH, self.licence_type1).send_keys('Attempted edit')

        current_value = self.get_attribute_value('value', self.licence_type)
        print(current_value)

        # Check if the value has changed after attempting to edit
        if current_value == initial_value:
            print("licence Text field is not editable.")
            assert True
        else:
            print("licence Text field is editable.")
            assert False

    def check_ips_field_is_editable(self):
        dropdown = self.driver.find_element(By.XPATH, self.add_field_dropdown)
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)
        time.sleep(5)
        dropdown.click()
        self.click(self.ip_checkbox)
        if " Warning " in self.driver.page_source:
            self.click(self.yes_button)
            time.sleep(3)
            self.click(self.ip_checkbox)
            initial_value = self.get_attribute_value('value', self.ips_field)
            print(initial_value)

            self.driver.find_element(By.XPATH, self.ips_field1).send_keys('Attempted edit')

            current_value = self.get_attribute_value('value', self.ips_field)
            print(current_value)

            # Check if the value has changed after attempting to edit

            if current_value != initial_value:
                print("ips Text field is  editable.")
                assert True
            else:
                print("ips field is not editable.")
                assert False
        else:
            self.click(self.ip_checkbox)
            element = self.driver.find_element(By.XPATH, self.details_page_submit_button)
            element.click()
            self.click(self.details_page_submit_button)
            initial_value = self.get_attribute_value('value', self.ips_field)
            print(initial_value)

            self.driver.find_element(By.XPATH, self.ips_field1).send_keys('Attempted edit')

            current_value = self.get_attribute_value('value', self.ips_field)
            print(current_value)

            # Check if the value has changed after attempting to edit

            if current_value != initial_value:
                print("ips Text field is  editable.")
                assert True
            else:
                print("ips field is not editable.")
                assert False

    def check_inbound_field_is_editable(self):
        dropdown = self.driver.find_element(By.XPATH, self.add_field_dropdown)
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)
        time.sleep(5)
        dropdown.click()
        self.click(self.inbound_checkbox)
        if " Warning " in self.driver.page_source:
            self.click(self.yes_button)
            time.sleep(3)
            self.click(self.inbound_checkbox)
            initial_value = self.get_attribute_value('value', self.inbound_field)
            print(initial_value)

            self.driver.find_element(By.XPATH, self.inbound_field1).send_keys('Attempted edit')

            current_value = self.get_attribute_value('value', self.inbound_field)
            print(current_value)

            # Check if the value has changed after attempting to edit

            if current_value != initial_value:
                print("inbound Text field is  editable.")
                assert True
            else:
                print("inbound field is not editable.")
                assert False
        else:
            self.click(self.inbound_checkbox)
            element = self.driver.find_element(By.XPATH, self.details_page_submit_button)
            element.click()
            self.click(self.details_page_submit_button)
            initial_value = self.get_attribute_value('value', self.inbound_field)
            print(initial_value)

            self.driver.find_element(By.XPATH, self.inbound_field1).send_keys('Attempted edit')

            current_value = self.get_attribute_value('value', self.inbound_field)
            print(current_value)

            # Check if the value has changed after attempting to edit

            if current_value != initial_value:
                print("inbound Text field is  editable.")
                assert True
            else:
                print("inbound field is not editable.")
                assert False

    def check_outbound_field_is_editable(self):
        dropdown = self.driver.find_element(By.XPATH, self.add_field_dropdown)
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)
        time.sleep(5)
        dropdown.click()
        self.click(self.outbound_checkbox)
        if " Warning " in self.driver.page_source:
            self.click(self.yes_button)
            time.sleep(3)
            self.click(self.outbound_checkbox)
            initial_value = self.get_attribute_value('value', self.outbound_field)
            print(initial_value)

            self.driver.find_element(By.XPATH, self.outbound_field1).send_keys('Attempted edit')

            current_value = self.get_attribute_value('value', self.outbound_field)
            print(current_value)

            # Check if the value has changed after attempting to edit

            if current_value != initial_value:
                print("outbound Text field is  editable.")
                assert True
            else:
                print("outbound field is not editable.")
                assert False
        else:
            print("else loop")
            self.click(self.outbound_checkbox)
            element = self.driver.find_element(By.XPATH, self.details_page_submit_button)
            element.click()
            self.click(self.details_page_submit_button)
            initial_value = self.get_attribute_value('value', self.outbound_field)
            print(initial_value)

            self.driver.find_element(By.XPATH, self.outbound_field1).send_keys('Attempted edit')

            current_value = self.get_attribute_value('value', self.outbound_field)
            print(current_value)

            # Check if the value has changed after attempting to edit

            if current_value != initial_value:
                print("outbound Text field is  editable.")
                assert True
            else:
                print("outbound field is not editable.")
                assert False
