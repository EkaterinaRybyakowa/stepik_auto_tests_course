from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    total = num1 + num2

    dropdown = Select(browser.find_element(By.TAG_NAME, "select"))
    dropdown.select_by_value(str(total))  # Преобразуем в строку!

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
