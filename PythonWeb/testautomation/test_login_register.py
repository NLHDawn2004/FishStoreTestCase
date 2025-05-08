import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FishStoreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Hoặc Firefox, Edge tùy bạn
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000")  # URL của project FishStore bạn đang chạy

    def test_user_signup_login_add_to_cart(self):
        driver = self.driver

        # 1. Bấm vào nút Đăng nhập
        login_button = driver.find_element(By.XPATH, "//a[text()='ĐĂNG NHẬP']")
        login_button.click()
        time.sleep(1)

        # 2. Chuyển sang Sign Up
        signup_button = driver.find_element(By.XPATH, "//a[text()='Sign up']")
        signup_button.click()
        time.sleep(1)

        # 3. Điền form đăng ký
        driver.find_element(By.NAME, "username").send_keys("user1")
        driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
        driver.find_element(By.NAME, "password1").send_keys("user123")
        driver.find_element(By.NAME, "password2").send_keys("user123")
        driver.find_element(By.XPATH, "//input[@type='submit' and @value='Đăng kí']").click()

        time.sleep(2)

        # 4. Đăng nhập sau khi đăng ký
        driver.find_element(By.NAME, "username").send_keys("user1")
        driver.find_element(By.NAME, "password").send_keys("user123")
        driver.find_element(By.XPATH, "//input[@type='submit' and @value='ĐĂNG NHẬP']").click()

        time.sleep(2)

    #     # 5. Thêm 3 sản phẩm vào giỏ hàng (giả định có các nút "Thêm vào giỏ" với class cụ thể)
    #     product_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Thêm vào giỏ')]")
        
    #     for i in range(3):
    #         product_buttons[i].click()
    #         time.sleep(1)

    #     # 6. Kiểm tra giỏ hàng có 3 sản phẩm
    #     cart_link = driver.find_element(By.LINK_TEXT, "Giỏ hàng")
    #     cart_link.click()
    #     time.sleep(2)

    #     items = driver.find_elements(By.CLASS_NAME, "cart-item")  # Giả định mỗi sản phẩm có class này
    #     self.assertEqual(len(items), 3, "Không đủ 3 sản phẩm trong giỏ hàng!")

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":
    unittest.main()