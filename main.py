from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

print(f'The title of the page is :{driver.title}')
print(f'The current url of the page is :{driver.current_url}')

text= driver.find_element(By.XPATH,'//*[@id="name"]')
text.clear()
text.send_keys("Samyok Poudyal")


driver.quit()


