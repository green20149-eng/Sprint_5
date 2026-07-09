import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators


class TestLoginsUser:

    def test_login_user(self, driver):

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Авторизация существующим пользователем
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("ruslan_nev_35@gmail.com")
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("2517Rus")
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        # Проверка успешной авторизации
        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LoginPageLocators.PROFILE_ICON)
        )
        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LoginPageLocators.PROFILE_NAME)
        )

    def test_logout_user(self, driver):

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Авторизация существующим пользователем
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("ruslan_nev_35@gmail.com")
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("2517Rus")
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        # Проверка успешной авторизации
        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LoginPageLocators.PROFILE_ICON)
        )
        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LoginPageLocators.PROFILE_NAME)
        )

        # Выход из личного кабинета
        driver.find_element(*LoginPageLocators.LOGOUT_BUTTON).click()

        # Проверка выхода
        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
