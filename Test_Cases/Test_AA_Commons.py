import logging
import time

from PageObjects.AAcommons import AAcommons
from Utilities import CustomLogger
from Utilities.readProperties import ReadConfig


class TestAACommons:
    aacommons = None

    logger = CustomLogger.setup_logger('AA_commons', ReadConfig.get_logs_directory() + "/Test_AA_commons.log",
                                       level=logging.DEBUG)

    def test_homepage(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        if "Central Registry Entries" in self.driver.page_source:
            assert True
            self.logger.info("Expected behavior: Homepage should display.")
        else:
            self.logger.error("Unexpected behavior: Homepage is not displayed.")
            assert False
        self.logger.info("********************test_homepage completed*********************")

    def test_central_registry_entries_present(self, setup):
        self.logger.info("*************Test_002_test_central_registry_entries_present*********************")
        self.logger.info("********************test_central_registry_entries_present started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        self.AA_commons.check_column_entry()
        self.logger.info("********************test_central_registry_entries_present ended*********************")

    def test_pop_up_screen(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        self.AA_commons.click_edit_button()
        if "Enter the Endpoint details that you're looking for" in self.driver.page_source:
            assert True
        else:
            assert False

    def test_autofill_text_field(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_edit_button()
        self.AA_commons.get_text_field_value()

    def test_text_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_edit_button()
        self.AA_commons.check_text_fill_is_editable()

    def test_alert_message(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_edit_button()
        self.AA_commons.check_alert_message()

    def test_autofilled_clientid_name(self, setup):
        self.logger.info("***********************Test_002_Homepage*****************************")
        self.logger.info("********************test_autofilled_clientid_name started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        self.AA_commons.compare_autofilled_clientid_with_id_name()

    def test_count_error_messages(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_edit_button()
        time.sleep(2)
        self.AA_commons.count_error_message()

    def test_cannot_find_your_entity_pop_up_screen(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        self.AA_commons.click_cannot_find_your_entity()
        if "Enter the Endpoint details that you're looking for" in self.driver.page_source:
            assert True
        else:
            assert False

    def test_secret_key_text_field(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_edit_button()
        self.AA_commons.check_secret_text_fill_is_editable()

    def test_submit_button(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_edit_button()
        time.sleep(3)
        self.AA_commons.enter_correct_secret_key()
        self.AA_commons.click_submit_button()
        time.sleep(3)
        if "AA Details" in self.driver.page_source:
            assert True
        else:
            assert False

    def test_modification_success_message(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_edit_button()
        self.AA_commons.enter_correct_secret_key()
        time.sleep(2)
        self.AA_commons.click_submit_button()
        time.sleep(4)
        self.AA_commons.check_modified_suucessfull_alert_message()

    def test_client_id_text_field_CFE(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_cannot_find_your_entity()
        time.sleep(2)
        self.AA_commons.check_client_id_text_field_is_editable()

    def test_secret_key_text_field_CFE(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_cannot_find_your_entity()
        time.sleep(2)
        self.AA_commons.check_secret_text_fill_is_editable()

    def test_pop_up_message_exit(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_login_page()
        time.sleep(2)
        self.AA_commons.click_cannot_find_your_entity()
        time.sleep(2)
        self.AA_commons.click_submit_button()
        if "Enter the Endpoint details that you're looking for" in self.driver.page_source:
            assert True
        else:
            assert False

    def test_back_button(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        self.AA_commons.open_details_page()
        self.AA_commons.click_back_button()
        if "Central Registry Entries" in self.driver.page_source:
            assert True
        else:
            assert False
        self.driver.quit()
        self.logger.info("********************test_homepage completed*********************")

    def test_certificate_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_certificate_field_is_editable()

    def test_base_url_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_base_url_field_is_editable()

    def test_entity_info_name_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_entity_info_name_field_is_editable()

    def test_entity_info_id_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_entity_info_id_field_is_editable()

    def test_entity_info_code_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_entity_info_code_field_is_editable()

    def test_entity_handle_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_entity_handle_field_is_editable()

    def test_web_view_url_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_web_view_url_field_is_editable()

    def test_regulated_name_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_regulated_name_field_is_editable()

    def test_category_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_category_field_is_editable()

    def test_licence_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        self.AA_commons.check_licence_field_is_editable()

    def test_ips_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        time.sleep(5)
        self.AA_commons.check_ips_field_is_editable()

    def test_inbound_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        time.sleep(5)
        self.AA_commons.check_inbound_field_is_editable()

    def test_outbound_field_editable_or_not(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.AA_commons = AAcommons(self.driver)
        time.sleep(2)
        self.AA_commons.open_details_page()
        time.sleep(5)
        self.AA_commons.check_outbound_field_is_editable()
