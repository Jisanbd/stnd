from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
import time


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        cls.driver.implicitly_wait(30)
        cls.base_url = "https://mcswiss-web-stage.web.app/"
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
