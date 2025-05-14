import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FishStoreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000")  # Đổi nếu bạn chạy ở port khác

    def test_login_and_add_3_products(self):
        driver = self.driver

        # 1. Vào trang Đăng nhập
        login_button = driver.find_element(By.XPATH, "//a[text()='ĐĂNG NHẬP']")
        login_button.click()
        time.sleep(1)

        # 2. Nhập thông tin đăng nhập
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("1234")
        driver.find_element(By.XPATH, "//input[@type='submit' and @value='ĐĂNG NHẬP']").click()
        time.sleep(2)

        # 3. Kéo xuống để hiện sản phẩm
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.3);")
        time.sleep(2)


        driver.find_element(By.XPATH, '/html/body/div[4]/a').click()
        time.sleep(2)


        driver.find_element(By.XPATH, '//*[@id="id_name"]').send_keys("Cá kiếm ")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="id_price"]').send_keys("1000000")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="id_description"]').send_keys("Cá kiếm là một loài cá cảnh đẹp và phổ biến trong ngành nuôi cá cảnh.")
        time.sleep(2)
        file_input = driver.find_element(By.ID, "id_image")  # Change selector as needed

        file_path = r"D:\DH Store\fishgit\PythonWeb\product\static\product\images\kiem1.jpg"  # Use absolute path
        file_input.send_keys(file_path)
        time.sleep(2)
        button = driver.find_element(By.XPATH, '/html/body/div/form/button')
        button.click()
        time.sleep(2)
        
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        
        
         # Click vào ô tìm kiếm
        search_input = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/form/input[2]')
        search_input.click()

        # Gõ từ khóa "Bảy màu"
        search_input.send_keys("Cá kiếm")
        time.sleep(4)
        search_button = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/form/button')
        search_button.click()

        # Chờ kết quả hiện ra
        time.sleep(10)
