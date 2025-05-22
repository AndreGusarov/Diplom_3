from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.auth_user_page import AuthUser
from pages.password_recovery_page import PasswordRecoveryPage
from pages.user_profile_page import UserProfilePage
from pages.create_order_page import CreateOrderPage

class UIWorkerWeb(MainPage, AuthUser, PasswordRecoveryPage, UserProfilePage, CreateOrderPage):
    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators