import random
import time

import self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class Locators:
    google_placeholder = "//textarea[@aria-label='Search']"
    url="https://www.google.com/"
    guvi="guvi.in"
    guvi_link="//a[@href='https://www.guvi.in/']"



    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_url(self):
        self.driver.get(self.url)
    def type_in_google(self):

        google = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.google_placeholder)))
        google.send_keys(self.guvi)
        google.send_keys(Keys.ENTER)
    def click_guvi(self):

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.guvi_link))).click()





object=Locators()
object.click_url()
object.type_in_google()
object.click_guvi()
time.sleep(10)
