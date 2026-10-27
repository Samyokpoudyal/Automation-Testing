from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()


# 1. Switching to Frame using Web Element

frame = driver.find_element(
    By.XPATH,
    "//iframe"
)

driver.switch_to.frame(frame)


# Finding element inside frame
input_box = driver.find_element(
    By.XPATH,
    "//input[@type='text']"
)

input_box.send_keys("Hello Selenium")


# 2. Switching back to Main Page

driver.switch_to.default_content()


# 3. Switching to Frame using Index

driver.switch_to.frame(0)

input_box = driver.find_element(
    By.XPATH,
    "//input[@type='text']"
)

input_box.clear()
input_box.send_keys("Using Frame Index")


# Return to main page
driver.switch_to.default_content()



time.sleep(3)

driver.quit()