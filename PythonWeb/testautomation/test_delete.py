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
        driver.find_element(By.NAME, "username").send_keys("dang99438")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.XPATH, "//input[@type='submit' and @value='ĐĂNG NHẬP']").click()
        time.sleep(2)

        # 3. Kéo xuống để hiện sản phẩm
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5);")
        time.sleep(2)

        # 4. Thêm 3 sản phẩm đầu tiên
        buy1 = driver.find_element(By.XPATH, "(//a[contains(@class, 'add-to-cart') and contains(text(), 'Buy Now!')])[1]")
        buy1.click()
        time.sleep(3)

        buy2 = driver.find_element(By.XPATH, "(//a[contains(@class, 'add-to-cart') and contains(text(), 'Buy Now!')])[2]")
        buy2.click()
        time.sleep(3)

        buy3 = driver.find_element(By.XPATH, "(//a[contains(@class, 'add-to-cart') and contains(text(), 'Buy Now!')])[3]")
        buy3.click()
        time.sleep(3)

        # 5. Kéo lên đầu trang
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        # 6. Vào trang Giỏ hàng
        cart_link = driver.find_element(By.XPATH, "//a[@class='btn btn-outline-danger d-flex align-items-center']")
        cart_link.click()
        time.sleep(5)
        
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5);")
        time.sleep(5)
        
        
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(4)
        
        
        link = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/table/tbody/tr[1]/td[3]/a")
        link.click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5);")
        time.sleep(5)
        
        
      

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

