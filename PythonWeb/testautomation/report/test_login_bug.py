import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FishStoreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000")  

    def test_user_signup_login_add_to_cart(self):
        driver = self.driver
        login_button = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/a')
        time.sleep(1)
        login_button.click()
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()