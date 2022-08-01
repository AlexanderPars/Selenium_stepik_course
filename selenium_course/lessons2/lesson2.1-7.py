from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_ele = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    x = x_ele
    print(x)


    answ = calc(x)
    print(answ)


    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answ)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()
    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    radiobutton1.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла