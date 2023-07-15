import random
import time

import self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
class Home:
    # url="https://www.automationexercise.com/login"
    url="https://automationexercise.com/"
    login_email="//input[@data-qa='login-email']"
    password="//input[@data-qa='login-password']"
    login_button="//button[@data-qa='login-button']"
    test_cases_page="//a[@href='/test_cases']"
    testcases_page_locator="//[@content='Automation Exercise / Automation Practice / Practice website for automation / demo website for practice / dummy website for testing / testing website / dummy website for practice automation / API Testing / API automation']"
    product="//a[@href='/products']"
    search_product="//input[@id='search_product']"
    product_to_added="Winter Top"
    submit_search="//button[@id='submit_search']"
    self.wait = WebDriverWait(self.driver,timeout=10)

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def click_url(self):
        self.driver.get(self.url)
    def click_product(self):

        self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.product))).click()
    def click_search(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.search_product))).send_keys(self.product_to_added)
    def enter_search(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.submit_search))).click()

    def verify_searched_item(self):
        try:

            element = webdriver.find_element_by_xpath("//p[text()='Winter Top']")


            assert element.is_displayed(), "Element is not displayed"
            print("Element found and displayed!")
        except:
            # Handle the case when the element is not found
            print("Element not found")






    # def click_email(self):
    #
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (By.XPATH, self.login_email))).send_keys('numrahashmi1@gmail.com')
    # def click_password(self):
    #
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (By.XPATH, self.password))).send_keys('Cybercrime123')
    # def click_login(self):
    #
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (By.XPATH, self.login_button))).click()
    # def click_testcases(self):
    #
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(
    #             (By.XPATH, self.test_cases_page))).click()
    #     time.sleep(10)
    # def verify_page(self):
    #     try:
    #
    #         element = webdriver.find_element_by_xpath(self.testcases_page_locator)
    #
    #
    #         assert element.is_displayed(), "Element is not displayed"
    #         print("Element found and displayed!")
    #     except:
    #         # Handle the case when the element is not found
    #         print("Element not found")
object=Home()
object.click_url()
object.click_product()
object.click_search()
object.enter_search()
object.verify_searched_item()
# object.click_email()
# object.click_password()
# object.click_login()
# object.click_testcases()
# object.verify_page()