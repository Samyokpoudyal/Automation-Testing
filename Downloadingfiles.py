from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


# Download folder
download_path = "C:\\Downloads"


# Chrome download preferences
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}


# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)


# Launch Chrome
driver = webdriver.Chrome(options=options)
driver.maximize_window()


# Open download page
driver.get("https://the-internet.herokuapp.com/download")


# Click file to download
download_file = driver.find_element(By.LINK_TEXT, "some-file.txt")
download_file.click()


# Wait for download to complete
time.sleep(5)


# Verify file download
file_path = os.path.join(download_path, "some-file.txt")

if os.path.exists(file_path):
    print("File downloaded successfully.")
else:
    print("File download failed.")


driver.quit()