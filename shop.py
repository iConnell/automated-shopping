from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

os.environ["PATH"] += r"C:\Users\Connell\Documents\Projs\Jango\scraping"

driver = webdriver.Chrome()


# Open webpage
driver.get('https://rahulshettyacademy.com/angularpractice/shop')

# Find the product (iphoneX)
product_name = driver.find_element(By.LINK_TEXT, 'iphone X')

# Find the parent of the whole product property
product = product_name.find_element(By.XPATH, 'parent::h4/parent::div/parent::div')

# Find and click the add to cart button
product.find_element(By.XPATH, '//div[@class="card-footer"]/button').click()

# Find and click the checkout button
driver.find_element(By.PARTIAL_LINK_TEXT, 'Checkout').click()

# Find and click the checkout button
driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()

# Fill in the delivery country
driver.find_element(By.XPATH, '//input[@id="country"]').send_keys('Germany')

# It takes time for suggestions to appear, so we have to wait for it
wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="suggestions"]')))

# Select US from the dropdown
driver.find_element(By.LINK_TEXT, 'Germany').click()

# Tick the checkbox
driver.find_element(By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()

# Click Purchase
driver.find_element(By.XPATH, '//input[@value="Purchase"]').click()

