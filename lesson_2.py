from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

link = 'https://www.selenium.dev/'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
time.sleep(3)

# Поиск элемента на странице по XPATH
element = browser.find_element(By.XPATH, '//*[@id="Layer_1"]')
# Скриншот элемента
element.screenshot(f"{os.path.dirname(__file__)}/scr/logo.png")

element = browser.find_element(By.XPATH, \
    '//input[@src="https://www.paypal.com/en_US/i/btn/btn_donateCC_LG.gif"]')

# Скролл к элементу
browser.execute_script('arguments[0].scrollIntoView();', element)
time.sleep(3)
browser.quit()