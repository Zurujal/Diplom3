import allure
import data

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Клик на кнопку Личный кабинет")
    def click_on_profile_button(self):
        locator = MainPageLocators.PROFILE_BUTTON
        self.click_on_element(locator)

    @allure.step("Клик на кнопку Лента заказов")
    def click_on_order_history_button(self):
        locator = MainPageLocators.ORDER_HISTORY
        self.click_on_element(locator)

    @allure.step("Клик на кнопку Конструктор")
    def click_on_builder_button(self):
        locator = MainPageLocators.BUILDER_BUTTON
        self.click_on_element(locator)

    @allure.step("Открытие деталей флюоресцентной булки")
    def open_ingredient_details(self):
        locator = MainPageLocators.FLUORESCENT_BUN
        self.click_on_element(locator)

    @allure.step("Нажатие на иконку крестика")
    def click_on_cross_button(self):
        locator = MainPageLocators.CROSS_BUTTON
        self.wait_for_element(locator)
        self.click_on_element(locator)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient(self):
        locator_from = MainPageLocators.FLUORESCENT_BUN
        locator_to = MainPageLocators.ADD_AREA
        self.drag_and_drop(locator_from, locator_to)

    @allure.step("Нажатие на кнопку Оформить заказ")
    def click_on_confirm_order_button(self):
        locator = MainPageLocators.CONFIRM_ORDER
        self.click_on_element(locator)

    @allure.step("Нажатие на элемент в истории заказов")
    def click_on_element_of_order_history(self):
        locator = MainPageLocators.ORDER_HISTORY_ELEMENT
        self.click_on_element(locator)

    @allure.step("Проверка наличия слова Состав в окне")
    def check_if_contains_presented(self):
        locator = MainPageLocators.CONTAINS_HEADER
        return self.get_text_from_element(locator) == data.CONTAINS

    @allure.step("Проверка успешно оформленного заказа")
    def check_if_order_successful(self):
        locator = MainPageLocators.SUCCESSFUL_ORDER
        return self.get_text_from_element(locator) == data.CONFIRMED_ORDER

    @allure.step("Проверка изменения каунтера")
    def check_if_counter_contains_2(self):
        locator = MainPageLocators.COUNTER
        return self.get_text_from_element(locator) == data.COUNTER

    @allure.step("Проверка перехода в Конструктор")
    def check_if_builder_transfer_ok(self):
        locator = MainPageLocators.CREATE_BURGER_HEADER
        return self.get_text_from_element(locator) == data.BURGER_HEADER

    @allure.step("Проверка перехода в Ленту заказов")
    def check_if_order_history_transfer_ok(self):
        locator = MainPageLocators.ORDER_HISTORY_HEADER
        return self.get_text_from_element(locator) == data.ORDER_HISTORY_HEADER

    @allure.step("Проверка открытия модального окна деталей ингридиента")
    def check_if_ingredient_details_opened(self):
        locator = MainPageLocators.INGREDIENT_HEADER
        return self.get_text_from_element(locator) == data.INGREDIENT_HEADER

    @allure.step("Ждем модального окна")
    def wait_for_modal(self):
        locator = MainPageLocators.CROSS_BUTTON
        return self.find_element_with_wait(locator)

    @allure.step("Номер заказа")
    def order_number(self):
        locator = MainPageLocators.ORDER_ID_LOCATOR
        self.wait_for_text_switch(locator, data.VALUE)
        return str(self.get_text_from_element(locator))
