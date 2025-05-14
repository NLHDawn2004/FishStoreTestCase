import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FishStoreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Hoặc Firefox, Edge tùy bạn
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000")  # URL của project FishStore bạn đang chạy

    def test_user_signup_login_add_to_cart(self):
        driver = self.driver

        # 1. Bấm vào nút Đăng nhập
        login_button = driver.find_element(By.XPATH, "//a[text()='ĐĂNG NHẬP']")
        login_button.click()
        time.sleep(1)
        
        driver.find_element(By.NAME, "username").send_keys("dang99438")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.XPATH, "//input[@type='submit' and @value='ĐĂNG NHẬP']").click()

        time.sleep(2)
        

        # 1. Click vào ô tìm kiếm
        search_input = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/form/input[2]')
        search_input.click()

        # 2. Gõ từ khóa "Bảy màu"
        search_input.send_keys("Bảy màu")
        time.sleep(4)
        search_button = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/form/button')
        search_button.click()

        # 4. Chờ kết quả hiện ra
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()