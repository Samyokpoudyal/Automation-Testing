from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


download_path = "C:\\Downloads"


prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}


options = webdriver.EdgeOptions()
options.add_experimental_option("prefs", prefs)


driver = webdriver.Edge(options=options)

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/download")


driver.find_element(
    By.LINK_TEXT,
    "some-file.txt"
).click()


time.sleep(5)


file_path = os.path.join(download_path, "some-file.txt")

if os.path.exists(file_path):
    print("File downloaded successfully.")
else:
    print("File download failed.")


driver.quit()