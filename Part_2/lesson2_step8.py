from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Петров")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@example.com")

    file_input = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    with open(file_path, 'w') as f:
        f.write("Это тестовый файл")

    file_input.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

    if os.path.exists(file_path):
        os.remove(file_path)