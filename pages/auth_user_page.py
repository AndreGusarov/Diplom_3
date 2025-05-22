import allure

from data.user_data import DataPerson
from web_locators.locators import LoginLocators, MainPageLocators
from pages.base_page import BasePage

class AuthUser(BasePage):
    @allure.step('Переход на форму авторизации по кнопке "Войти в аккаунт"')
    def click_personal_account_button(self):
       self.move_to_element_and_click(MainPageLocators.LOGIN_PROFILE_BUTTON)

    @allure.step('Проверка перехода на страницу Авторизации')
    def check_switch_on_login_page(self):
        self.wait_until_element_is_visible(LoginLocators.LOGIN_TEXT)
        return self.get_current_url()

    @allure.step('Заполнение поля "email"')
    def set_email_field(self, user_email):
        self.wait_until_element_is_visible(LoginLocators.EMAIL_FIELD).click()
        self.set_text_to_element(LoginLocators.EMAIL_FIELD, user_email)

    @allure.step('Заполнение поля "password"')
    def set_password_field(self, user_password):
        self.set_text_to_element(LoginLocators.PASSWORD_FIELD, user_password)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        self.click_element(LoginLocators.LOGIN_BUTTON_ANY_FORMS)
        self.wait_element_to_be_clickable(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Авторизация')
    def login(self):
        self.click_personal_account_button()
        self.set_email_field(DataPerson.user_login)
        self.set_password_field(DataPerson.user_password)
        self.click_login_button()
