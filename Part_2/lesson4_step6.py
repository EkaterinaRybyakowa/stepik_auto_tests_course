from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

# Этот вызов вызовет NoSuchElementException
element = browser.find_element(By.ID, "button")