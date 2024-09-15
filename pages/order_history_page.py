import allure

from pages.base_page import BasePage
from locators.order_history_page_locators import OrderHistoryPageLocators


class OrderHistoryPage(BasePage):
    @allure.step("Всего заказов")
    def all_time_counter(self):
        locator = OrderHistoryPageLocators.DONE_ALL_TIME_LOCATOR
        return str(self.get_text_from_element(locator))

    @allure.step("Всего сегодня")
    def today_counter(self):
        locator = OrderHistoryPageLocators.TODAY_LOCATOR
        return str(self.get_text_from_element(locator))


    @allure.step("Номера заказов")
    def today_orders(self):
        locator = OrderHistoryPageLocators.ORDERS
        return str(self.get_text_from_element(locator))
