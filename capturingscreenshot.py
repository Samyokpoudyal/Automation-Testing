from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()


# 1. Capture Full Page Screenshot
driver.save_screenshot("homepage.png")


# 2. Capture Screenshot using get_screenshot_as_file()
driver.get_screenshot_as_file("tutorialninja.png")


# 3. Capture Screenshot as PNG
png_data = driver.get_screenshot_as_png()

print("PNG Screenshot Captured")


# 4. Capture Screenshot as Base64
base64_data = driver.get_screenshot_as_base64()

print("Base64 Screenshot Captured")


# 5. Capture Screenshot of a Web Element
logo = driver.find_element(By.CLASS_NAME, "img-responsive")

logo.screenshot("logo.png")


time.sleep(2)

driver.quit()