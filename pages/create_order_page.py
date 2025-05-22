import allure

from web_locators.locators import OrdersPageLocators
from pages.base_page import BasePage


class CreateOrderPage(BasePage):
    @allure.step('Нажимаем на заказ в списке Лента заказов')
    def click_order(self):
        self.wait_element_to_be_clickable(OrdersPageLocators.ORDER_LINK).click()

    @allure.step('Проверка состава заказа')
    def check_order_structure(self):
        return self.check_presence(OrdersPageLocators.ORDER_STRUCTURE).is_displayed()

    @allure.step("Проверка совпадения заказов в истории и в ленте")  
    def check_order_id(self, order_id, locator):
        elements = self.wait_until_all_elements_located(locator)
        order_id_with_hash = f"#0{order_id}" 
    
        for element in elements:
            text = element.text.strip()
            if order_id_with_hash == text:
                return True
        return False    

    @allure.step("Проверка нахождение идентификатора заказа в истории")
    def is_order_id_found_at_history(self, order_number):
        return self.check_order_id(order_number, OrdersPageLocators.ALL_ORDERS_AT_HISTORY)

    @allure.step("Проверка нахождение идентификатора заказа в ленте")
    def is_order_id_found_at_feed(self, order_number):
        return self.check_order_id(order_number, OrdersPageLocators.ALL_ORDERS_AT_FEED)

    @allure.step("Получение количества заказов")
    def get_total_order_count_daily(self, locator):
        return self.get_actual_text(locator)

    @allure.step('Получение номера заказа')
    def get_user_order(self, orders_numbers):
        order = f'0{orders_numbers}'
        self.wait_text_to_be_present_in_element(OrdersPageLocators.NUMBER_IN_PROGRESS, order)
        return order
    
    @allure.step('Получение номера заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_actual_text(OrdersPageLocators.NUMBER_IN_PROGRESS)