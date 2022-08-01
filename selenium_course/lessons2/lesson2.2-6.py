from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math



try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 150)")
    time.sleep(1)
    # browser.execute_script("document.getElementById('bd-footer').style.display = 'none'")
    x_ele = browser.find_element(By.XPATH, "/html/body/div//div//*[@id = 'input_value']")

    x = x_ele.text
    print(x)
    print(calc(x))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()
    # browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox1)
    # browser.execute_script("window.scrollBy(0, 50);")
    radiobutton1 = browser.find_element(By.ID, "robotsRule")

    radiobutton1.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла