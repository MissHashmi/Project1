from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class Prices:
    url = "https://www.letskodeit.com/practice"
    prices ="//span[@class='currency']"
    list_prices=[]

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def click_url(self):
        self.driver.get(self.url)

    def get_prices(self):

        elements=WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH, "//td[@class='price']")))
        for element in elements:
            element.text
            print(element)

object=Prices()
object.click_url()
object.get_prices()
