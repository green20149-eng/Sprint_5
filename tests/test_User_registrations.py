import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from selenium.webdriver.support.wait import WebDriverWait
import uuid

class TestUserRegistrations:

    def test_user_registration(self, driver):

        driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*RegistrationPageLocators.NO_ACCOUNT_BUTTON).click()

        email = f"user_{uuid.uuid4().hex[:8]}@mail.ru"

        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("Test123@")
        driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).send_keys("Test123@")
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.PROFILE_ICON
            )
        )

        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.PROFILE_NAME
            )
        )

    def test_user_registration_Error_email(self, driver):

        driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*RegistrationPageLocators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("Test@@2027.mail.ru")
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("Test123@")
        driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).send_keys("Test123@")
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.ERROR_TITLE
            )
        )

        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.EMAIL_ERROR
            )
        )

        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.PASSWORD_ERROR
            )
        )

    def test_registration_existing_user(self, driver):

        driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*RegistrationPageLocators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("Test20266@mail.ru")
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("Test20266")
        driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT).send_keys("Test20266")
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.ERROR_TITLE
            )
        )

        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.EMAIL_ERROR
            )
        )

        assert WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(
                RegistrationPageLocators.PASSWORD_ERROR
            )
        )
