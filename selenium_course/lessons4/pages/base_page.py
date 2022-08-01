from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:

    def __int__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        try:
            self.browser = webdriver.Chrome()
            self.browser.get(self.url)
        except:
            pass
