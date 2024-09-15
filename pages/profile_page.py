import allure

import data
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step('Проверка наличия кнопки Войти')
    def check_if_enter_button_presented(self):
        locator = ProfilePageLocators.ENTER_BUTTON
        return self.get_text_from_element(locator) == data.ENTER_BUTTON

    @allure.step('Проверка наличия кнопки Восстановить')
    def check_if_restore_button_presented(self):
        locator = ProfilePageLocators.RESTORE_BUTTON
        return self.get_text_from_element(locator) == data.RESTORE_BUTTON

    @allure.step('Проверка наличия хедера лента заказов')
    def check_if_order_page(self):
        locator = ProfilePageLocators.ORDER_PAGE_HEADER
        return self.get_text_from_element(locator) == data.ORDER_PAGE_HEADER

    @allure.step('Проверка наличия кнопки Сохранить')
    def check_if_save_button_presented(self):
        locator = ProfilePageLocators.SAVE_BUTTON
        return self.get_text_from_element(locator) == data.SAVE_BUTTON

    @allure.step('Проверка что поле стало активным')
    def check_if_field_is_active(self):
        locator = ProfilePageLocators.ACTIVE_FIELD_LOCATOR
        return self.get_text_from_element(locator) == data.PASSWORD_CHECK

    @allure.step('Нажатие кнопки Выход')
    def click_logout_button(self):
        locator = ProfilePageLocators.EXIT_BUTTON
        return self.click_on_element(locator)

    @allure.step('Нажатие кнопки Войти')
    def click_enter_button(self):
        locator = ProfilePageLocators.ENTER_BUTTON
        return self.click_on_element(locator)

    @allure.step('Нажатие на поле показать/скрыть пароль')
    def click_eye_field(self):
        locator = ProfilePageLocators.FIELD_LOCATOR
        return self.click_on_element(locator)

    @allure.step('Нажате кнопки Восстановить пароль')
    def click_restore_password_button(self):
        locator = ProfilePageLocators.RESTORE_PASSWORD_BUTTON
        return self.click_on_element(locator)

    @allure.step('Нажате кнопки Восстановить')
    def click_restore_button(self):
        locator = ProfilePageLocators.RESTORE_BUTTON
        return self.click_on_element(locator)

    @allure.step('Ввод Email')
    def fill_email_field(self):
        locator = ProfilePageLocators.EMAIL_INPUT_FIELD
        self.set_text_to_element(locator, data.EMAIL)

    @allure.step('Ввод пароля')
    def fill_password_field(self):
        locator = ProfilePageLocators.PASSWORD_INPUT_FIELD
        self.set_text_to_element(locator, data.PASSWORD)
