from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://qa-desk.education-services.ru/")

driver.find_element(By.XPATH, "//button[contains(text(),'Вход и регистрация')]").click()


#Авотризация существующим пользователем
driver.find_element(By.NAME, "email").send_keys("ruslan_nev_35@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("2517Rus")
driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

#Проверка, что успешно авторизировались
assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@class='circleSmall']//*[name()='svg']")))
assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//h3[@class='profileText name']")))

driver.quit()
