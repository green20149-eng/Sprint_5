import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLoginsUser:
    def test_login_user(self, driver):

            driver.find_element(By.XPATH, "//button[contains(text(),'Вход и регистрация')]").click()


#Авотризация существующим пользователем
            driver.find_element(By.NAME, "email").send_keys("ruslan_nev_35@gmail.com")
            driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("2517Rus")
            driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

#Проверка, что успешно авторизировались
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@class='circleSmall']//*[name()='svg']")))
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//h3[@class='profileText name']")))

    def test_logout_user(self, driver):

            driver.find_element(By.XPATH, "//button[contains(text(),'Вход и регистрация')]").click()


#Авотризация существующим пользователем
            driver.find_element(By.NAME, "email").send_keys("ruslan_nev_35@gmail.com")
            driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("2517Rus")
            driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

#Проверка, что успешно авторизировались
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@class='circleSmall']//*[name()='svg']")))
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//h3[@class='profileText name']")))

#Выход из личного кабинета
            driver.find_element(By.XPATH, "//button[contains(text(),'Выйти')]").click()

#Проверка, что вышли из личного кабинета
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[contains(text(),'Вход и регистрация')]")))
