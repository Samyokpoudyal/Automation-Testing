from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector


driver = webdriver.Chrome()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

cursor = connection.cursor()

cursor.execute(
    "SELECT email, password FROM users WHERE id=1"
)

user = cursor.fetchone()


driver.find_element(
    By.ID,
    "input-email"
).send_keys(user[0])

driver.find_element(
    By.ID,
    "input-password"
).send_keys(user[1])

driver.find_element(
    By.XPATH,
    "//input[@value='Login']"
).click()


cursor.close()
connection.close()

driver.quit()