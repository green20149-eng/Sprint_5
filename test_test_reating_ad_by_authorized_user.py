from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa-desk.education-services.ru/")

driver.find_element(By.XPATH, "//button[contains(text(),'Вход и регистрация')]").click()


#Авотризация существующим пользователем
driver.find_element(By.NAME, "email").send_keys("ruslan_nev_35@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("2517Rus")
driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

#Проверка, что успешно авторизировались
assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@class='circleSmall']//*[name()='svg']")))

#Создание объявления
driver.find_element(By.XPATH, "//button[contains(text(),'Разместить объявление')]").click()

#Проверка, что открылась форма добавление объявления
assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"//h1[@class='hi createListing_title__IFtFs']")))

#Заполнение объявления
driver.find_element(By.XPATH, "//input[@placeholder='Название']").send_keys("Хорошая книга")
driver.find_element(By.XPATH, "//textarea[@placeholder='Описание товара']").send_keys("Продам Хорошую книгу")
driver.find_element(By.XPATH, "//input[@placeholder='Стоимость']").send_keys("1000")

#Заполнение выпадающих форм
driver.find_element(By.CLASS_NAME, "dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP").click()
assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='dropDownMenu_options__CmHmm']//button[1]")))
driver.find_element(By.XPATH, "//div[@class='dropDownMenu_options__CmHmm']//button[1]").click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.find_element(By.XPATH, "//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']//*[name()='svg']").click()
assert WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Новосибирск')]")))
driver.find_element(By.XPATH, "//span[contains(text(),'Новосибирск')]").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.quit()
