from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os



try:

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "text.txt"
    file_path = os.path.join(current_dir, file_name)

    print(file_name)
    print(file_path)

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk@123.com")
    input4 = browser.find_element(By.CSS_SELECTOR, "[type='file']")

    input4.send_keys(file_path)
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла