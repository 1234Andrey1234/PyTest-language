import pytest
import time
from selenium import webdriver

def test_basket_button_exist(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    
    browser.get(url)
    
    time.sleep(30)
    Button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    #Ждем 30 секунд
    assert len(Button) == 1
