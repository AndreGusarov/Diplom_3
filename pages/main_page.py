import allure

from web_locators.locators import *
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Переход по кнопке "Личный кабинет"')
    def click_personal_account(self):
        self.move_to_element_and_click(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Переход на страницу "Лента заказов"')
    def click_orders_list_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDERS_LIST_BUTTON)
        self.wait_until_element_is_visible(OrdersPageLocators.ORDERS_LIST_TITLE)
    
    @allure.step('Переход в конструктор')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_until_element_is_visible(MainPageLocators.MAIN_LIST_TITLE)
    
    @allure.step('Клик на ингредиент')
    def click_ingredient(self):
        self.wait_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT).click()

    @allure.step('Проверка всплывающего окна с ингредиентами')
    def check_details_ingredient_form_is_displayed(self):
        self.wait_until_element_is_visible(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.get_actual_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)
    
    @allure.step('Закрыть форму с ингридиентами с помощью Х')
    def click_cross_button(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)

    @allure.step('Проверка, что окно с ингредиентами закрылось')
    def invisibility_ingredient_details(self):
        self.check_element_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Проверка отображения ингредиентов на экране')
    def check_ingredient_details_are_displayed(self):
        return self.check_presence(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    @allure.step('Получение значения счетчика ингредиента')
    def get_count_value(self):
        return self.get_actual_text(MainPageLocators.INGREDIENT_COUNTER)
    
    @allure.step('Добавление ингредиента в заказ')
    def add_filling_to_order(self):
        self.wait_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step('Нажатие кнопки "Оформить заказ"')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_until_element_is_visible(MainPageLocators.ORDER_IDENTIFICATE)

    @allure.step('Проверка, что заказ оформлен и появился идентификатор заказа')
    def check_show_window_with_order_id(self):
        self.wait_until_element_is_visible(MainPageLocators.ORDER_IDENTIFICATE)
        return self.get_actual_text(MainPageLocators.ORDER_IDENTIFICATE)

    @allure.step('Получение ORDER_ID')
    def get_with_order_id(self):
        self.wait_until_element_is_visible(MainPageLocators.ORDER_IDENTIFICATE)
        order_id = self.get_actual_text(MainPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_actual_text(MainPageLocators.ORDER_ID)
        return f"{order_id}"
        
    @allure.step("Проверка открытия модального окна")
    def modal_box_is_open(self):
        return self.check_presence(MainPageLocators.ORDER_ID)

    @allure.step('Проверить наличие, что заказа начали готовить')
    def check_displayed_order_status_text(self):
        return self.check_presence(MainPageLocators.ORDER_STATUS_TEXT).is_displayed()

    @allure.step("Закрыть модальное окно после создания заказа")
    def click_close_modal_order(self):
        self.wait_element_to_be_clickable(MainPageLocators.CLOSE_MODAL_ORDER)
        """self.click_element(MainPageLocators.CLOSE_MODAL_ORDER)"""
        self.move_to_element_and_click(MainPageLocators.CLOSE_MODAL_ORDER)
    
