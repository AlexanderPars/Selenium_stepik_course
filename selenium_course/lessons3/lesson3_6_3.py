import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By





links_array = ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"]





@pytest.mark.parametrize('links', links_array)
def test_guest_should_see_login_link(browser, links):
    answer = math.log(int(time.time()))
    link = f"{links}"
    browser.get(link)
    browser.implicitly_wait(6)
    browser.find_element(By.CSS_SELECTOR, ".ember-text-area").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    assert "Correct!" in result.text, "Error in correction checking!"
