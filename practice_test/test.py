import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Locators:
    car_select = "//select[@id='carselect']"
    multiple_select = "//option[@value='orange']"
    radio_button = "//input[@id='bmwradio']"
    alert_example = "//input[@id='name']"
    open_window = "//button[@id='openwindow']"
    disable_button ="//input[@id='disabled-button']"
    auto_suggest ="//input[@id='autosuggest']"
    check_box = "//input[@id='bmwcheck']"
    element_displayed_place_holder="//input[@id='displayed-text']"
    mouse_hover_top ="//a[@href='#top']"


    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_car_select_button(self):

        cars = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH, self.car_select)))
        car=random.choice(cars)
        car.click()
    def click_multiple_select_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.multiple_select))).click()


