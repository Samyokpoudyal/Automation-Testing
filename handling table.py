from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# Locate Table
table = driver.find_element(By.ID, "productTable")


# Read Table Headers
headers = table.find_elements(By.TAG_NAME, "th")

print("Table Headers:")

for header in headers:
    print(header.text)



# Read All Rows and Columns

rows = table.find_elements(By.TAG_NAME, "tr")

print("Table Data:")

for row in rows:

    columns = row.find_elements(By.TAG_NAME, "td")

    for column in columns:
        print(column.text)

    print("----------------")



# Count Rows

print("Total Rows:", len(rows))



# Count Columns

columns = table.find_elements(By.TAG_NAME, "th")

print("Total Columns:", len(columns))



time.sleep(3)

driver.quit()