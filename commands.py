from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Application Command
driver.get("https://testautomationpractice.blogspot.com/")

print("Title:", driver.title)
print("URL:", driver.current_url)

# Browser Command
driver.maximize_window()

# Navigation Commands
driver.refresh()
driver.back()
driver.forward()

# Conditional Commands
name = driver.find_element(By.XPATH, '//*[@id="name"]')

print("Displayed:", name.is_displayed())
print("Enabled:", name.is_enabled())

if name.is_displayed():
    name.send_keys("Samyok Poudyal")

driver.quit()