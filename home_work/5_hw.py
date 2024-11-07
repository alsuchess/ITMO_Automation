# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def check_elements():
#
#     driver = webdriver.Chrome()
#     driver.get("https://www.saucedemo.com/")
#
#     username = driver.find_element(By.CSS_SELECTOR, '#user-name')
#     password = driver.find_element(By.CSS_SELECTOR, '#password')
#     submit = driver.find_element(By.CSS_SELECTOR, '#login-button')
#
#     # Проверка, найдены ли все элементы
#     if username and password and submit:
#         print('Элементы найдены')
#     else:
#         print('Не все элементы найдены')

#check_elements()

from selenium import webdriver
from selenium.webdriver.common.by import By

def check_elements(url, field1, field2, field3):

    driver = webdriver.Chrome()
    driver.get(url)

    username = driver.find_element(By.CSS_SELECTOR, field1)
    password = driver.find_element(By.CSS_SELECTOR, field2)
    submit = driver.find_element(By.CSS_SELECTOR, field3)

    # Проверка, найдены ли все элементы
    if username and password and submit:
        print('Элементы найдены')
    else:
        print('Не все элементы найдены')

check_elements("https://www.saucedemo.com/", '#user-name', '#password', '#login-button')