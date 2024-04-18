import logging
import time

from PageObjects.login import Login
from Utilities import CustomLogger
from Utilities.readProperties import ReadConfig


class Testlogin:
    loginpage = None

    logger = CustomLogger.setup_logger('Login', ReadConfig.get_logs_directory() + "/Test_login.log",
                                       level=logging.DEBUG)

    def test_homepage(self, setup):
        self.logger.info("***********************Test_001_Homepage*****************************")
        self.logger.info("********************test_homepage started*********************")
        self.driver = setup
        self.loginpage = Login(self.driver)
        self.driver.maximize_window()
        self.loginpage.open_login_page()
        if "Central Registry Entries" in self.driver.page_source:
            assert True
        else:
            assert False
        self.logger.info("********************test_homepage completed*********************")

    def test_autofilled_clientid_name(self, setup):
        self.logger.info("***********************Test_002_Homepage*****************************")
        self.logger.info("********************test_autofilled_clientid_name started*********************")
        self.driver = setup
        self.loginpage = Login(self.driver)
        self.driver.maximize_window()
        self.loginpage.open_login_page()
        self.loginpage.compare_autofilled_clientid_with_id_name()

    def test_FIU_kpi_value(self, setup):
        self.logger.info("***********************Test_003_Homepage*****************************")
        self.logger.info("********************test_FIU_kpi_value started*********************")
        self.driver = setup
        self.loginpage = Login(self.driver)
        self.loginpage.open_login_page()
        self.loginpage.validate_fiu_kpi_value()
