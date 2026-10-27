from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# 1. Scroll Down by 500 Pixels
driver.execute_script("window.scrollBy(0,500)")
time.sleep(2)


# 2. Scroll Up by 300 Pixels
driver.execute_script("window.scrollBy(0,-300)")
time.sleep(2)


# 3. Scroll to Bottom of the Page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)


# 4. Scroll to Top of the Page
driver.execute_script("window.scrollTo(0,0)")
time.sleep(2)


# 5. Scroll Until an Element is Visible
element = driver.find_element(By.ID, "footer")

driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)


# 6. Horizontal Scroll
driver.execute_script("window.scrollBy(500,0)")
time.sleep(2)


driver.quit()