

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math



try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # говорим WebDriver ждать все элементы в течение 12 секунд
    # browser.implicitly_wait(12)


    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    # browser.execute_script("window.scrollBy(0, 50)")



    x_ele = browser.find_element(By.ID, "input_value")

    x = x_ele.text
    print(x)
    print(calc(x))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    button = browser.find_element(By.ID, "solve")

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла