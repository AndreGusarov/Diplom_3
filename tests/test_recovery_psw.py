import allure
import pytest

from data.urls import Urls
from data.user_data import DataPerson
from pages import UIWorkerWeb


class TestRecoveryPsw:
    @allure.title('Проверка перехода на Восстановить пароль')
    def test_click_password_reset_button(self, pages: UIWorkerWeb):
        pages.click_personal_account()
        pages.click_password_reset_link()
        current_url = pages.get_current_url()
        assert current_url == Urls.RESTORE_PSW_PAGE

    @allure.title('Проверка ввода почты и переход после клика по кнопке "Восстановить"')
    def test_enter_email_and_click_reset(self, pages: UIWorkerWeb):
        pages.open_link(Urls.RESTORE_PSW_PAGE)
        pages.set_email_for_reset_password(DataPerson.user_login)
        pages.click_reset_button()
        pages.find_save_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.RESET_PSW_PAGE

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_make_field_active(self, pages: UIWorkerWeb):
        pages.open_link(Urls.RESTORE_PSW_PAGE)
        pages.set_email_for_reset_password(DataPerson.user_login)
        pages.click_reset_button()
        pages.find_save_button()
        pages.click_on_show_password_button()
        assert pages.find_input_active()