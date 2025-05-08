import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FishStoreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000")  

    def test_user_signup_login_add_to_cart(self):
        driver = self.driver
        # 1. Bấm vào nút Đăng nhập
        login_button = driver.find_element(By.XPATH, "//a[text()='ĐĂNG NHẬP']")
        login_button.click()
        time.sleep(1)
        
        driver.find_element(By.NAME, "username").send_keys("user1")
        driver.find_element(By.NAME, "password").send_keys("user12333")
        driver.find_element(By.XPATH, "//input[@type='submit' and @value='ĐĂNG NHẬP']").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()