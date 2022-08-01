import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Тест должен провалиться. ответ на задание: FAILED (errors=1)
class TestAbs():

    def test_abs1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            self.browser = webdriver.Chrome()
            self.browser.get(link)

            self.input1 = self.browser.find_element(By.CSS_SELECTOR, ".first[required]")
            self.input1.send_keys("Ivan")
            self.input2 = self.browser.find_element(By.CSS_SELECTOR, ".second[required]")
            self.input2.send_keys("Petrov")

            self.input3 = self.browser.find_element(By.CSS_SELECTOR, ".third[required]")
            self.input3.send_keys("1234@mail.ru")

            # Отправляем заполненную форму
            self.button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
            self.button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            self.welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            self.welcome_text = self.welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert ("Congratulations! You have successfully registered!", self.welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            self.browser.quit()


    def test_abs2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            self.browserinput1 = browser.find_element(By.CSS_SELECTOR, ".first[required]")
            self.browserinput1.send_keys("Ivan")
            self.browserinput2 = browser.find_element(By.CSS_SELECTOR, ".second[required]")
            self.browserinput2.send_keys("Petrov")

            self.browserinput3 = browser.find_element(By.CSS_SELECTOR, ".third[required]")
            self.browserinput3.send_keys("1234@mail.ru")

            # Отправляем заполненную форму
            self.browserbutton = browser.find_element(By.CSS_SELECTOR, "button.btn")
            self.browserbutton.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            self.browserwelcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            self.browserwelcome_text = self.welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert ("Congratulations! You have successfully registered!", self.welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
