from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()


actions = ActionChains(driver)


# 1. Mouse Hover

components = driver.find_element(
    By.LINK_TEXT,
    "Components"
)

actions.move_to_element(components).perform()



# 2. Left Click

search = driver.find_element(
    By.ID,
    "input-search"
)

actions.click(search).perform()



# 3. Double Click

element = driver.find_element(
    By.XPATH,
    "//h2[text()='Featured']"
)

actions.double_click(element).perform()



# 4. Right Click

actions.context_click(element).perform()



# 5. Drag and Drop

driver.get("https://demoqa.com/droppable")

source = driver.find_element(
    By.ID,
    "draggable"
)

target = driver.find_element(
    By.ID,
    "droppable"
)

actions.drag_and_drop(
    source,
    target
).perform()



# 6. Click and Hold + Release

actions.click_and_hold(source).perform()

actions.release().perform()



# 7. Move Mouse by Offset

actions.move_by_offset(
    100,
    50
).perform()



time.sleep(3)

driver.quit()