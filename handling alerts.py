from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()


# 1. Switching to Alert
# driver.switch_to.alert is used to switch Selenium control from the webpage to the JavaScript alert popup.

driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Alert']"
).click()

alert = driver.switch_to.alert



# 2. Accepting Alert
# alert.accept() is used to click the OK button on an alert popup.

alert.accept()



# 3. Dismissing Alert
# alert.dismiss() is used to click the Cancel button on a confirmation alert.

driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Confirm']"
).click()

alert = driver.switch_to.alert

alert.dismiss()



# 4. Getting Alert Text
# alert.text is used to retrieve the message displayed inside the alert popup.

driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Alert']"
).click()

alert = driver.switch_to.alert

message = alert.text

print(message)

alert.accept()



# 5. Sending Text to Prompt Alert
# alert.send_keys() is used to enter text into a prompt alert input box.

driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Prompt']"
).click()

alert = driver.switch_to.alert

alert.send_keys("Selenium")

alert.accept()



time.sleep(3)

driver.quit()