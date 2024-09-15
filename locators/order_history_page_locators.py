from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    DONE_ALL_TIME_LOCATOR = By.XPATH, '(//*[@class="OrderFeed_number__2MbrQ text text_type_digits-large"])[1]'
    TODAY_LOCATOR = By.XPATH, '(//*[@class="OrderFeed_number__2MbrQ text text_type_digits-large"])[2]'
    ORDERS = By.XPATH, '//*[@class="OrderFeed_orderList__cBvyi"]'