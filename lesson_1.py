from selenium import webdriver # Импорт вебдрайвера
import time, os

# URL's
page_1 = 'https://www.selenium.dev/'
page_2 = 'https://www.selenium.dev/downloads/'
page_3 = 'https://www.selenium.dev/projects/'
page_4 = 'https://www.selenium.dev/documentation/'

# Actions 
browser = webdriver.Chrome()  # Иницализация вебрайвера с браузером Chrome
browser.maximize_window() # Открывает окно браузера в максимальном размере
browser.get(page_1) # Открытие нужного URL
time.sleep(1) # Дает время увидеть результат работы скрипта

browser.get(page_2) # Открытие нужного URL
window_1st = browser.current_window_handle # Возвращает дескриптор текущего окна
time.sleep(1) # Дает время увидеть результат работы скрипта

browser.back() # команда, чтобы вернуться назад
time.sleep(1) # Дает время увидеть результат работы скрипта

browser.forward() # команда, чтобы идти вперед
time.sleep(1) # Дает время увидеть результат работы скрипта

browser.refresh() # команда, обновить страницу
time.sleep(1) # Дает время увидеть результат работы скрипта

browser.switch_to.new_window('tab') # открывает новую вкладку браузера
browser.get(page_3) # Открытие нужного URL

time.sleep(1) # Дает время увидеть результат работы скрипта

print(browser.title) # Возвращает заголовок текущей страницы
print(browser.current_url) # Получает URL-адрес текущей страницы.

browser.switch_to.new_window('window') # открывает новое окно браузера
browser.get(page_4)
time.sleep(1)

browser.close() # Закрывает текущее окно браузера
time.sleep(1)

browser.switch_to.window(window_1st) # Переключает фокус на указанное окно
time.sleep(1)
# --------------------------------------------------------------------------

browser.get(page_1)
time.sleep(1)

browser.switch_to.new_window('tab')
browser.get(page_2)
time.sleep(1)

browser.switch_to.new_window('tab')
browser.get(page_3)
time.sleep(1)

browser.switch_to.new_window('tab')
browser.get(page_4)
time.sleep(1)


while len(browser.window_handles) - 1:
    browser.switch_to.window(browser.window_handles[-1])
    browser.close()


browser.switch_to.window(browser.window_handles[0])
browser.save_screenshot(f"{os.path.dirname(__file__)}/scr/foo1.png")


time.sleep(3)
browser.quit() # Закрытие процесса браузера