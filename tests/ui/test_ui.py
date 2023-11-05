import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке буде вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemaill.com")

    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pas_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pas_elem.send_keys("wrong password")

    #Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Імітуємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми осікуємо
    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(3) 

   #Закриваємо браузер
    driver.close()
    
