from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


download_path = "C:\\Downloads"


options = webdriver.FirefoxOptions()

options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", download_path)
options.set_preference(
    "browser.helperApps.neverAsk.saveToDisk",
    "application/octet-stream,text/plain,application/pdf"
)
options.set_preference("pdfjs.disabled", True)


driver = webdriver.Firefox(options=options)

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