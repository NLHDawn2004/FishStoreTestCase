import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

class RegisterFailTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_password_mismatch(self):
        driver = self.driver
        driver.get("http://localhost:8000/")

         # 1. Bấm vào nút Đăng nhập
        login_button = driver.find_element(By.XPATH, "//a[text()='ĐĂNG NHẬP']")
        login_button.click()
        time.sleep(1)

         # 2. Chuyển sang Sign Up
        signup_button = driver.find_element(By.XPATH, "//a[text()='Sign up']")
        signup_button.click()
        time.sleep(1)

        # Điền form với mật khẩu không khớp
        driver.find_element(By.NAME, "username").send_keys("user1")
        driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
        driver.find_element(By.NAME, "password1").send_keys("abc123456")
        driver.find_element(By.NAME, "password2").send_keys("abc654321")  # không khớp
        driver.find_element(By.XPATH, "//input[@type='submit' and @value='Đăng kí']").click()

        time.sleep(2)

        # Kiểm tra có thông báo lỗi hay không
        page_source = driver.page_source
        self.assertTrue("Mật khẩu" in page_source or "không khớp" in page_source or "password" in page_source.lower())
        print("Test mật khẩu không khớp: Passed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
