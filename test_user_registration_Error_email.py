from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_user_registration_Error_email():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")

    driver.find_element(By.XPATH, "//button[contains(text(),'Вход и регистрация')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Нет аккаунта')]").click()

    driver.find_element(By.NAME, "email").send_keys("Test@@2027.mail.ru")
    driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("Test123@")
    driver.find_element(By.XPATH, "//input[@placeholder='Повторите пароль']").send_keys("Test123@")
    driver.find_element(By.XPATH, "//button[contains(text(),'Создать аккаунт')]").click()

    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Ошибка')]")))
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='popUp_inputColumn__RgD8n']//div[2]//div[1]//div[1]")))
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='homePage_modal__zSdUB']//div[3]//div[1]//div[1]")))
    driver.quit()

test_user_registration_Error_email()