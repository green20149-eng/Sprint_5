from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

    PROFILE_ICON = (
        By.XPATH,
        "//button[@class='circleSmall']//*[name()='svg']"
    )
    PROFILE_NAME = (
        By.XPATH,
        "//h3[@class='profileText name']"
    )

    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]")

class CreateAdLocators:
    CREATE_AD_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Разместить объявление')]"
    )

    AUTH_MODAL_TITLE = (
        By.XPATH,
        "//h1[@class='h1']"
    )

    CREATE_AD_TITLE = (
        By.XPATH,
        "//h1[@class='hi createListing_title__IFtFs']"
    )

    TITLE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Название']"
    )

    DESCRIPTION_INPUT = (
        By.XPATH,
        "//textarea[@placeholder='Описание товара']"
    )

    PRICE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Стоимость']"
    )

    CATEGORY_DROPDOWN = (
        By.XPATH,
        "//button[contains(@class,'dropDownMenu_arrowDown')]"
    )

    FIRST_CATEGORY = (
        By.XPATH,
        "//div[@class='dropDownMenu_options__CmHmm']//button[1]"
    )

    CITY_DROPDOWN = (
        By.XPATH,
        "(//button[contains(@class,'dropDownMenu_arrowDown')])[2]"
    )

    NOVOSIBIRSK = (
        By.XPATH,
        "//span[contains(text(),'Новосибирск')]"
    )

    SUBMIT_AD_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

class RegistrationPageLocators:
    # Кнопки
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Вход и регистрация')]"
    )

    NO_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Нет аккаунта')]"
    )

    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Создать аккаунт')]"
    )

    # Поля ввода
    EMAIL_INPUT = (
        By.NAME,
        "email"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@placeholder='Пароль']"
    )

    REPEAT_PASSWORD_INPUT = (
        By.XPATH,
        "//input[@placeholder='Повторите пароль']"
    )

    # Успешная регистрация
    PROFILE_ICON = (
        By.XPATH,
        "//button[@class='circleSmall']//*[name()='svg']"
    )

    PROFILE_NAME = (
        By.XPATH,
        "//h3[@class='profileText name']"
    )

    # Ошибки
    ERROR_TITLE = (
        By.XPATH,
        "//span[contains(text(),'Ошибка')]"
    )

    EMAIL_ERROR = (
        By.XPATH,
        "//div[@class='popUp_inputColumn__RgD8n']//div[2]//div[1]//div[1]"
    )

    PASSWORD_ERROR = (
        By.XPATH,
        "//div[@class='homePage_modal__zSdUB']//div[3]//div[1]//div[1]"
    )