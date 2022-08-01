import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

answer = math.log(int(time.time()))
print(answer)

link = "https://stepik.org/lesson/236895/step/1"




try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(6)
    browser.find_element(By.CSS_SELECTOR, ".ember-text-area").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    print(result.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

