from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_reating_ad_by_unauthorized_user():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")

#Нажимаем на кнопку "разместить побъявление" без авториации
    driver.find_element(By.XPATH, "//button[contains(text(),'Разместить объявление')]").click()

#Проверка что открыто модлаьное окно с заголовком "Чтобы разместить объявление атворизируйтесь"
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"//h1[@class='h1']")))
    driver.quit()

test_reating_ad_by_unauthorized_user()