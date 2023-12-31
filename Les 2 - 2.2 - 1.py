from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc():
    return str(int(x) + int(y))


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = x_element.text

    y_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = y_element.text

    z = calc()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(z)


    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
