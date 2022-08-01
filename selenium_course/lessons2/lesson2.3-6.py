from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math



try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_window = browser.window_handles[0]
    button1 = browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    time.sleep(1)

    x_ele = browser.find_element(By.ID, "input_value")

    x = x_ele.text
    print(x)
    print(calc(x))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла