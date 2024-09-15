from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON = By.XPATH, '//*[text()="Личный Кабинет"]'
    ORDER_HISTORY = By.XPATH, '//*[text()="Лента Заказов"]'
    BUILDER_BUTTON = By.XPATH, '//*[text()="Конструктор"]'
    ENTER_PROFILE_BUTTON = By.XPATH, '//*[text()="Войти в аккаунт"]'
    CREATE_BURGER_HEADER = By.XPATH, '//*[@class = "text text_type_main-large mb-5 mt-10"]'
    ORDER_HISTORY_HEADER = By.XPATH, '//*[@class = "text text_type_main-large mt-10 mb-5"]'
    FLUORESCENT_BUN = By.XPATH, '(//*[@class="BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4"])[1]'
    INGREDIENT_HEADER = By.XPATH, '//*[@class = "Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"]'
    CROSS_BUTTON = By.XPATH, '//*[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
    ADD_AREA = By.XPATH, '//*[@class = "constructor-element constructor-element_pos_top"]'
    COUNTER = By.XPATH, '//*[@class = "counter_counter__num__3nue1"]'
    CONFIRM_ORDER = By.XPATH, '//*[text()="Оформить заказ"]'
    SUCCESSFUL_ORDER = By.XPATH, '//*[@class = "undefined text text_type_main-small mb-2"]'
    ORDER_HISTORY_ELEMENT = By.XPATH, '//*[@class = "OrderHistory_listItem__2x95r mb-6"]'
    CONTAINS_HEADER = By.XPATH, '//*[@class = "text text_type_main-medium mb-8"]'
    ORDER_ID_LOCATOR = By.XPATH, '//*[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'




