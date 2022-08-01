from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math



try:
    def calc(num1, num2):
        return str(int(num1) + int(num2))

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_ele = browser.find_element(By.ID, "num1")
    num1 = num1_ele.text
    print(num1)
    num2_ele = browser.find_element(By.ID, "num2")
    num2 = num2_ele.text
    print(num2)
    print(type(int(num2)))


    answ = calc(num1, num2)
    print(answ)


    ch_list = Select(browser.find_element(By.TAG_NAME, "select"))
    ch_list.select_by_value(answ)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла