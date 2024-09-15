import allure


class TestProfilePage:

    @allure.title("Проверка возможности выхода из аккаунта")
    def test_logout(self, main_page, profile_page):
        main_page.click_on_profile_button()
        profile_page.fill_email_field()
        profile_page.fill_password_field()
        profile_page.click_enter_button()
        main_page.click_on_profile_button()
        profile_page.click_logout_button()
        assert profile_page.check_if_enter_button_presented() is True

    @allure.title("Проверка перехода на страницу восстановления пароля")
    def test_restore_password_transition(self, main_page, profile_page):
        main_page.click_on_profile_button()
        profile_page.click_restore_password_button()
        assert profile_page.check_if_restore_button_presented() is True

    @allure.title("Ввод почты и клик на кнопку Восстановить")
    def test_enter_mail_and_click_on_restore_button(self, main_page, profile_page):
        main_page.click_on_profile_button()
        profile_page.click_restore_password_button()
        profile_page.fill_email_field()
        profile_page.click_restore_button()
        assert profile_page.check_if_save_button_presented() is True

    @allure.title("клик по кнопке показать/скрыть пароль делает поле активным")
    def test_click_on_eye_icon_make_field_active(self, main_page, profile_page):
        main_page.click_on_profile_button()
        profile_page.click_restore_password_button()
        profile_page.fill_email_field()
        profile_page.click_restore_button()
        profile_page.click_eye_field()
        assert profile_page.check_if_field_is_active() is True
