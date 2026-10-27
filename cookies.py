from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()


# 1. Get All Cookies

cookies = driver.get_cookies()

print("All Cookies:")

for cookie in cookies:
    print(cookie)



# 2. Get a Specific Cookie

cookie = driver.get_cookie("currency")

print("Specific Cookie:")

print(cookie)



# 3. Add a New Cookie

driver.add_cookie({
    "name": "username",
    "value": "selenium"
})

print("Cookie Added")



# 4. Delete a Specific Cookie

driver.delete_cookie("username")

print("Cookie Deleted")



# 5. Delete All Cookies

driver.delete_all_cookies()

print("All Cookies Deleted")


time.sleep(2)

driver.quit()