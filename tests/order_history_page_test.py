import allure


class TestOrderHistoryPage:

    @allure.title("Проверка нажатия на заказ в ленте заказов")
    def test_click_on_order_history_element(self, main_page):
        main_page.click_on_order_history_button()
        main_page.click_on_element_of_order_history()
        assert main_page.check_if_contains_presented() is True

    @allure.title("При создании нового заказа счетчик выполнено за все время увеличивается")
    def test_all_time_counter(self, main_page, profile_page, order_history_page):
        main_page.click_on_profile_button()
        profile_page.fill_email_field()
        profile_page.fill_password_field()
        profile_page.click_enter_button()
        main_page.add_ingredient()
        main_page.click_on_confirm_order_button()
        order_id = main_page.order_number()
        main_page.click_on_cross_button()
        main_page.click_on_order_history_button()
        all_orders = order_history_page.all_time_counter()
        assert order_id == all_orders

    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_today_counter(self, main_page, profile_page, order_history_page):
        main_page.click_on_profile_button()
        profile_page.fill_email_field()
        profile_page.fill_password_field()
        profile_page.click_enter_button()
        main_page.add_ingredient()
        main_page.click_on_confirm_order_button()
        order_id = main_page.order_number()
        main_page.click_on_cross_button()
        main_page.click_on_order_history_button()
        today_orders = order_history_page.today_counter()
        assert order_id != today_orders

    @allure.title("после оформления заказа его номер появляется в разделе В работе")
    def test_order_number_exists(self, main_page, profile_page, order_history_page):
        main_page.click_on_profile_button()
        profile_page.fill_email_field()
        profile_page.fill_password_field()
        profile_page.click_enter_button()
        main_page.add_ingredient()
        main_page.click_on_confirm_order_button()
        main_page.wait_for_modal()
        order_id = main_page.order_number()
        main_page.click_on_cross_button()
        main_page.click_on_order_history_button()
        today_orders = order_history_page.today_orders()
        assert order_id in today_orders
