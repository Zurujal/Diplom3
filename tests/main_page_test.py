import allure


class TestMainPage:

    @allure.title("Проверка возможности перехода в профиль по клику на «Личный кабинет»")
    def test_enter_profile(self, main_page, profile_page):
        main_page.click_on_profile_button()
        assert profile_page.check_if_enter_button_presented() is True

    @allure.title("Проверка возможности перехода в ленту заказов")
    def test_enter_order_history(self, main_page, profile_page):
        main_page.click_on_order_history_button()
        assert profile_page.check_if_order_page() is True

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_builder_click_transition(self, main_page):
        main_page.click_on_order_history_button()
        main_page.click_on_builder_button()
        assert main_page.check_if_builder_transfer_ok() is True

    @allure.title("Проверка перехода по клику на Лента Заказов")
    def test_order_history_click_transition(self, main_page):
        main_page.click_on_order_history_button()
        assert main_page.check_if_order_history_transfer_ok() is True

    @allure.title("Проверка что если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_open_ingredient_details(self, main_page):
        main_page.open_ingredient_details()
        assert main_page.check_if_ingredient_details_opened() is True

    @allure.title("Проверка возможности закрытия модального окна")
    def test_possibility_close_modal_window(self, main_page):
        main_page.open_ingredient_details()
        main_page.click_on_cross_button()
        assert main_page.check_if_builder_transfer_ok() is True

    @allure.title("Проверка увеличения каунтера при добавлении ингредиента")
    def test_counter(self, main_page):
        main_page.add_ingredient()
        assert main_page.check_if_counter_contains_2() is True

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_create_order(self, main_page, profile_page):
        main_page.click_on_profile_button()
        profile_page.fill_email_field()
        profile_page.fill_password_field()
        profile_page.click_enter_button()
        main_page.add_ingredient()
        main_page.click_on_confirm_order_button()
        assert main_page.check_if_order_successful() is True
