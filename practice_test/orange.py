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

    url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    user_name="//input[@name='username']"
    password="//input[@name='password']"
    submitt="//button[@type='submit']"
    admin_tab="//a[@href='/web/index.php/admin/viewAdminModule']"
    add="//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"

    user_role="//label[text()='User Role']//parent::div//following-sibling::div//div[@tabindex='0']"

    emp_user_name="//label[text()='Username']//parent::div//following-sibling::div//input[@autocomplete='off']"
    status="//label[text()='Status']//parent::div//following-sibling::div//div[@tabindex='0']"
    emp_password="//label[text()='Password']/parent::div/following-sibling::div/input[@type='password']"
    employe_name="//input[@placeholder='Type for hints...']"

    confirm_password="//label[text()='Confirm Password']//parent::div//following-sibling::div//input[@type='password']"
    logout="//a[@href='/web/index.php/auth/logout']"




    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def click_url(self):
        self.driver.get(self.url)
    def click_user_name(self):

        google = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.user_name)))
        google.send_keys('Admin')
        google.send_keys(Keys.ENTER)
    def click_password(self):

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.password))).send_keys('admin123')
    def click_login(self):

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.submitt))).click()

    def get_title(self):
        print(self.driver.title)

    def click_dropdown(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//span[@class='oxd-userdropdown-tab']"))).click()


    def click_admin(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.admin_tab))).click()
    def click_add(self):
         WebDriverWait(self.driver, 10).until(
             expected_conditions.element_to_be_clickable(
                 (By.XPATH, self.add))).click()
    def click_userrole(self):
         element= WebDriverWait(self.driver, 10).until(
             expected_conditions.element_to_be_clickable(
                 (By.XPATH, self.user_role)))
         element.send_keys(Keys.ARROW_DOWN)

    def click_employename(self):
         name=WebDriverWait(self.driver, 10).until(
             expected_conditions.element_to_be_clickable(
                 (By.XPATH, self.employe_name)))
         name.send_keys("num")
    def click_status(self):
         element= WebDriverWait(self.driver, 10).until(
             expected_conditions.element_to_be_clickable(
                 (By.XPATH, self.status)))
         element.send_keys(Keys.ARROW_DOWN)

    def click_emp_user_name(self):
        name = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.emp_user_name)))
        name.send_keys("num123")

    def click_emp_password(self):
         password = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.emp_password)))
         password.send_keys("S3cr3t")
    def click_confirm_password(self):
         password = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.confirm_password)))
         password.send_keys("S3cr3t")
    def click_save(self):
         password = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']"))).clcik()



    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.logout))).click()



object=Locators()
object.click_url()
object.click_user_name()
object.click_password()
object.click_login()
object.get_title()
object.click_dropdown()
object.click_admin()
object.click_add()
object.click_userrole()
object.click_employename()
object.click_emp_user_name()
object.click_status()
object.click_emp_user_name()
object.click_emp_password()
object.click_confirm_password()
object.click_save
time.sleep(10)
