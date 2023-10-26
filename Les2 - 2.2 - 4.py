from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input2 = browser.find_element(By.NAME, "firstname")
    input2.send_keys("Anna")
    input3 = browser.find_element(By.NAME, "lastname")
    input3.send_keys("Gorz")
    input4 = browser.find_element(By.NAME, "email")
    input4.send_keys("Gorz@dsf.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()