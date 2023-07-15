import random
import time

import self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class Flight:
    google_placeholder = "//textarea[@aria-label='Search']"
    url="https://www.google.com/"
    expedia="expedia.co.in"
    expedia_link="//a[@href='https://www.expedia.co.in/']"
    flights="//span[contains(text(),'Flights')]"
    search_box="//button[@aria-label='Leaving from']"
    textarea_searchbox="//input[@placeholder='Where are you leaving from?']"
    destination_search_box="//button[@aria-label='Going to']"



    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def click_url(self):
        self.driver.get(self.url)
    def type_in_google(self):

        google = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.google_placeholder)))
        google.send_keys(self.expedia)
        google.send_keys(Keys.ENTER)
    def click_expedia(self):

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.expedia_link))).click()
    def click_flights(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.flights))).click()

    def click_search_bar(self):
        element=WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.search_box))).click()
    def click_textarea_searchbox(self):
        element=WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH,self.textarea_searchbox)))
        element.send_keys("Delhi")
        time.sleep(5)

    def select_delhi(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='Delhi (DEL - Indira Gandhi Intl.) India']"))).clcik()

    def click_destination_search(self):
        element=WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.destination_search_box)))
        element.send_keys("Chenni")





object=Flight()
object.click_url()
object.type_in_google()
object.click_expedia()
object.click_flights()
object.click_search_bar()
object.click_textarea_searchbox()
object.select_delhi()
object.click_destination_search()

