from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()


# Locate Search Box
search_box = driver.find_element(By.NAME, "search")


# Type Text
search_box.send_keys("Laptop")

time.sleep(1)


# Select All (Ctrl + A)
search_box.send_keys(Keys.CONTROL, "a")

time.sleep(1)


# Copy (Ctrl + C)
search_box.send_keys(Keys.CONTROL, "c")

time.sleep(1)


# Cut (Ctrl + X)
search_box.send_keys(Keys.CONTROL, "x")

time.sleep(1)


# Paste (Ctrl + V)
search_box.send_keys(Keys.CONTROL, "v")

time.sleep(1)


# Press Enter
search_box.send_keys(Keys.ENTER)

time.sleep(2)


# Press Backspace
search_box.send_keys(Keys.BACKSPACE)

time.sleep(1)


# Press Delete
search_box.send_keys(Keys.DELETE)

time.sleep(1)


# Press Escape
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

time.sleep(1)


# Press Tab
search_box.send_keys(Keys.TAB)

time.sleep(2)

driver.quit()