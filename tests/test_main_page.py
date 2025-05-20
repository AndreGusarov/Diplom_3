import allure
import pytest

from data.urls import Urls
from pages import UIWorkerWeb


class TestMainPage:

    @allure.title('переход по клику на «Конструктор»')
    @allure.description('При нажатии в хедере кнопки "Конструктор" происходит переход на страницу конструктора')
    def test_go_to_constructor(self, pages: UIWorkerWeb):
        pages.click_orders_list_button()
        pages.click_constructor_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.MAIN_PAGE

    @allure.title('переход по клику на «Лента заказов»')
    @allure.description('При нажатии в хедере кнопки "Лента заказов" происходит переход на страницу с заказами')
    def test_redirection_to_order_list(self, pages: UIWorkerWeb):
        pages.click_orders_list_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.FEED_PAGE
    
    @allure.title('При нажатии на ингридиент появляется всплывающее окно с деталями')
    @allure.description('При нажатии на игридиент всплывает модальное окно с информацией об ингридиенте')
    def test_popup_of_ingredient(self, pages: UIWorkerWeb):
        pages.click_ingredient()
        actually_text = pages.check_details_ingredient_form_is_displayed()
        assert actually_text == "Детали ингредиента"

    @allure.title('При нажатии Х всплывающее окно закрывается')
    @allure.description('При нажатии на Х в правом верхнем углу, всплывающее окно закрылось')
    def test_close_ingredient_details_window(self, pages: UIWorkerWeb):
        pages.click_ingredient()
        pages.click_cross_button()
        pages.invisibility_ingredient_details()
        assert pages.check_ingredient_details_are_displayed() == False

    @allure.title('При добавлении ингридиента в заказ, счетчик увеличивается')
    @allure.description('При добавлении ингридиента счетчик ингридента увеличился')
    def test_ingredient_counter(self, pages: UIWorkerWeb):
        prev_counter_value = pages.get_count_value()
        pages.add_filling_to_order()
        actual_value = pages.get_count_value()
        assert actual_value > prev_counter_value

    @allure.title('Проверка возможности оформления заказ авторизованным пользователем')
    @allure.description('При нажатии кнопки «Оформить заказ» заказ оформлен и появился идентификатор заказа')
    def test_successful_order(self, pages: UIWorkerWeb, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        actually_text = pages.check_show_window_with_order_id()
        assert actually_text == "идентификатор заказа" and pages.check_displayed_order_status_text() == True