#!./venv/bin/python
# -*- coding: utf-8 -*-

# Defines class TestPathways for pathways related web-page

# Standard library
import random
import string
import time
import unittest
from time import sleep

# Third-party
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# First-party
from pageObjects.flight import Flight


class TestFlight(unittest.TestCase):
    """Defines testcases for the pathway page"""

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('ignore-certificate-errors')

        cls.driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        )

    def test_a_check_the_title_of_page(self):
        """Tests if user is able to land on pathways page"""
        driver = self.driver
        driver.get(self.url)
        driver.object=Flight()
        Flight.click_url()
        Flight.type_in_google()
