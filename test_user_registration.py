from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import uuid

def test_user_registration():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")

    driver.find_element(By.XPATH, "//button[contains(text(),'Вход и регистрация')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Нет аккаунта')]").click()

    email = f"user_{uuid.uuid4().hex[:8]}@mail.ru"

    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("Test123@")
    driver.find_element(By.XPATH, "//input[@placeholder='Повторите пароль']").send_keys("Test123@")
    driver.find_element(By.XPATH, "//button[contains(text(),'Создать аккаунт')]").click()

    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@class='circleSmall']//*[name()='svg']")))
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//h3[@class='profileText name']")))
    driver.quit()

test_user_registration()