import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    treasure_img = browser.find_element(By.ID, "treasure")
    x_value = treasure_img.get_attribute("valuex")

    y = calc(x_value)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
