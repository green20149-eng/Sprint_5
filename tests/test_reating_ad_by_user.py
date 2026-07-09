import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, CreateAdLocators

class TestReatingsAdByUser:

    def test_reating_ad_by_unauthorized_user(self, driver):

        driver.find_element(*CreateAdLocators.CREATE_AD_BUTTON).click()

        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(CreateAdLocators.AUTH_MODAL_TITLE)
        )

    def test_test_reating_ad_by_authorized_user(self, driver):

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Авторизация
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("ruslan_nev_35@gmail.com")
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("2517Rus")
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        assert WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located(LoginPageLocators.PROFILE_ICON)
        )

        # Создание объявления
        driver.find_element(*CreateAdLocators.CREATE_AD_BUTTON).click()

        assert WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located(CreateAdLocators.CREATE_AD_TITLE)
        )

        driver.find_element(*CreateAdLocators.TITLE_INPUT).send_keys("Хорошая книга")
        driver.find_element(*CreateAdLocators.DESCRIPTION_INPUT).send_keys("Продам Хорошую книгу")
        driver.find_element(*CreateAdLocators.PRICE_INPUT).send_keys("1000")

        driver.find_element(*CreateAdLocators.CATEGORY_DROPDOWN).click()

        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located(CreateAdLocators.FIRST_CATEGORY)
        ).click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        driver.find_element(*CreateAdLocators.CITY_DROPDOWN).click()

        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located(CreateAdLocators.NOVOSIBIRSK)
        ).click()

        driver.find_element(*CreateAdLocators.SUBMIT_AD_BUTTON).click()
