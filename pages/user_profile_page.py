import allure

from web_locators.locators import UserProfileLocators
from pages.base_page import BasePage


class UserProfilePage(BasePage):

    @allure.step('Проверка перехода на страницу профиля')
    def check_switch_on_profile(self):
        self.wait_element_to_be_clickable(UserProfileLocators.PROFILE_BUTTON)
        return self.get_current_url()
    
    @allure.step('Нажимаем кнопку «История заказов»')
    def click_order_history_button(self):
        self.wait_element_to_be_clickable(UserProfileLocators.ORDER_HISTORY_BUTTON)
        self.click_element(UserProfileLocators.ORDER_HISTORY_BUTTON)
    
    @allure.step('Проверяем переход на страницу История заказов')
    def check_switch_on_order_history(self):
        self.wait_element_to_be_clickable(UserProfileLocators.ENABLED_ORDER_HISTORY_BUTTON)
        return self.get_current_url()

    @allure.step('Нажимаем кнопку «Выход»')
    def click_log_out_button(self):
        self.wait_element_to_be_clickable(UserProfileLocators.LOGOUT_BUTTON)
        self.click_element(UserProfileLocators.LOGOUT_BUTTON)