from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ENTER_BUTTON = By.XPATH, '//*[text()="Войти"]'
    EMAIL_INPUT_FIELD = By.XPATH, '//*[@type="text"]'
    PASSWORD_INPUT_FIELD = By.XPATH, '//*[@type="password"]'
    ORDER_PAGE_HEADER = By.XPATH, '//*[text()="Лента заказов"]'
    EXIT_BUTTON = By.XPATH, '//*[text()="Выход"]'
    RESTORE_PASSWORD_BUTTON = By.XPATH, '//*[text()="Восстановить пароль"]'
    RESTORE_BUTTON = By.XPATH, '//*[text()="Восстановить"]'
    SAVE_BUTTON = By.XPATH, '//*[text()="Сохранить"]'
    FIELD_LOCATOR = By.XPATH, '//*[@class="input__icon input__icon-action"]'
    ACTIVE_FIELD_LOCATOR = By.XPATH, '//*[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]'



