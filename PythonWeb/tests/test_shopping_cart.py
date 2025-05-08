import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8000"  # Update with your actual URL

    def test_user_registration_and_shopping(self):
        driver = self.driver
        
        # Step 1: Navigate to the homepage
        driver.get(self.base_url)
        
        # Step 2: Click on Login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập"))
        )
        login_button.click()
        
        # Step 3: Click on Sign Up link
        signup_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up"))
        )
        signup_link.click()
        
        # Step 4: Fill in registration form
        username_field = driver.find_element(By.NAME, "username")
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password1")
        confirm_password_field = driver.find_element(By.NAME, "password2")
        
        username_field.send_keys("user1")
        email_field.send_keys("user1@gmail.com")
        password_field.send_keys("user123")
        confirm_password_field.send_keys("user123")
        
        # Step 5: Click Register button
        register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        register_button.click()
        
        # Step 6: Login with registered credentials
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        
        username_field.send_keys("user1")
        password_field.send_keys("user123")
        
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Step 7: Add 3 products to cart
        # Assuming products are listed on the homepage
        add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "add-to-cart")[:3]
        
        for button in add_to_cart_buttons:
            button.click()
            time.sleep(1)  # Wait for cart to update
        
        # Verify cart has 3 items
        cart_count = driver.find_element(By.CLASS_NAME, "cart-count")
        self.assertEqual(cart_count.text, "3", "Cart should contain 3 items")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main() 