from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()


# 1. Finding Element by ID
# Locates element using the unique id attribute
element_id = driver.find_element(By.ID, "input-search")
element_id.send_keys("Laptop")


# 2. Finding Element by Name
# Locates element using the name attribute
element_name = driver.find_element(By.NAME, "search")
element_name.clear()
element_name.send_keys("Phone")


# 3. Finding Element by Class Name
# Locates element using the class attribute
element_class = driver.find_element(By.CLASS_NAME, "form-control")


# 4. Finding Element by XPath
# Locates element using XPath expression
element_xpath = driver.find_element(By.XPATH, "//input[@name='search']")


# 5. Finding Element by CSS Selector
# Locates element using CSS selector pattern
element_css = driver.find_element(By.CSS_SELECTOR, "input[name='search']")


# 6. Finding Element by Link Text
# Locates link using complete visible text
link_text = driver.find_element(By.LINK_TEXT, "Desktops")
link_text.click()


# 7. Finding Element by Partial Link Text
# Locates link using partial visible text
partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Desk")


# 8. Finding Element by Tag Name
# Locates element using HTML tag name
tag_name = driver.find_element(By.TAG_NAME, "h1")
print(tag_name.text)


# 9. Finding Multiple Elements
# Locates multiple elements using the same locator
multiple_elements = driver.find_elements(By.TAG_NAME, "a")

for element in multiple_elements:
    print(element.text)


time.sleep(3)

driver.quit()