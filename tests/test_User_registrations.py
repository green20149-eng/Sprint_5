import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import uuid

class TestUserRegistrations:
    def test_user_registration(self, driver):

            driver.find_element(By.XPATH, "//button[contains(text(),'Вход и регистрация')]").click()
            driver.find_element(By.XPATH, "//button[contains(text(),'Нет аккаунта')]").click()

            email = f"user_{uuid.uuid4().hex[:8]}@mail.ru"

            driver.find_element(By.NAME, "email").send_keys(email)
            driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("Test123@")
            driver.find_element(By.XPATH, "//input[@placeholder='Повторите пароль']").send_keys("Test123@")
            driver.find_element(By.XPATH, "//button[contains(text(),'Создать аккаунт')]").click()

            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@class='circleSmall']//*[name()='svg']")))
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//h3[@class='profileText name']")))

    def test_user_registration_Error_email(self, driver):

            driver.find_element(By.XPATH, "//button[contains(text(),'Вход и регистрация')]").click()
            driver.find_element(By.XPATH, "//button[contains(text(),'Нет аккаунта')]").click()

            driver.find_element(By.NAME, "email").send_keys("Test@@2027.mail.ru")
            driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("Test123@")
            driver.find_element(By.XPATH, "//input[@placeholder='Повторите пароль']").send_keys("Test123@")
            driver.find_element(By.XPATH, "//button[contains(text(),'Создать аккаунт')]").click()

            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Ошибка')]")))
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='popUp_inputColumn__RgD8n']//div[2]//div[1]//div[1]")))
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='homePage_modal__zSdUB']//div[3]//div[1]//div[1]")))

    def test_registration_existing_user(self, driver):

            driver.find_element(By.XPATH, "//button[contains(text(),'Вход и регистрация')]").click()
            driver.find_element(By.XPATH, "//button[contains(text(),'Нет аккаунта')]").click()

            driver.find_element(By.NAME, "email").send_keys("Test20266@mail.ru")
            driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("Test20266")
            driver.find_element(By.XPATH, "//input[@placeholder='Повторите пароль']").send_keys("Test20266")
            driver.find_element(By.XPATH, "//button[contains(text(),'Создать аккаунт')]").click()

            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Ошибка')]")))
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='popUp_inputColumn__RgD8n']//div[2]//div[1]//div[1]")))
            assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='homePage_modal__zSdUB']//div[3]//div[1]//div[1]")))
