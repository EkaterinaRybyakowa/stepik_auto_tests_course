from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test@example.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем успешность регистрации
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        return welcome_text

    finally:
        time.sleep(5)
        browser.quit()


# Тестируем на первой странице (должно пройти успешно)
print("Testing on registration1.html...")
result1 = test_registration("http://suninjuly.github.io/registration1.html")
print(f"Result: {result1}")

# Тестируем на второй странице (должно упасть с ошибкой)
print("Testing on registration2.html...")
try:
    result2 = test_registration("http://suninjuly.github.io/registration2.html")
    print(f"Result: {result2}")
    print("ERROR: Test passed on registration2.html but should have failed!")
except Exception as e:
    print(f"SUCCESS: Test failed as expected with error: {e}")