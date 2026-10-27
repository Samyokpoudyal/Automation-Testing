from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome()

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()


# 1. Implicit Wait
# Waits globally for elements to be available
driver.implicitly_wait(10)

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Laptop")


# 2. Explicit Wait
# Waits for a specific condition before performing an action
wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.presence_of_element_located((By.ID, "input-search"))
)


# 3. Presence of Element Located
# Waits until the element exists in the DOM
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search"))
)


# 4. Visibility of Element Located
# Waits until the element is visible on the webpage
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "input-search"))
)

driver.quit()


