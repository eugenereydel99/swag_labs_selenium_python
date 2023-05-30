import allure

from pages.base_page import BasePage
from utils.locators import LoginPageLocators


class LoginPage(BasePage):
    accepted_usernames: str = "standard_user"
    accepted_password: str = "secret_sauce"

    __epic_sadface_error_messages = [
        "Username is required",
        "Password is required",
        "Username and password do not match any user in this service"
    ]

    @allure.step(title="Проверка нахождения на странице авторизации")
    def __should_be_login_page(self):
        with allure.step(title="Проверка наличия логотипа"):
            assert self.is_element_visible(
                *LoginPageLocators.LOGIN_LOGO
            )

        with allure.step(title="Проверка наличия формы авторизации"):
            assert self.is_element_visible(
                *LoginPageLocators.LOGIN_FORM
            )

    @allure.step(title="Заполнение формы авторизации")
    def __fill_credentials_for_authorize(self, username: str, password: str):
        self.__should_be_login_page()
        with allure.step(title="Проверка наличия поля ввода логина и ввод данных"):
            self.is_element_visible(
                *LoginPageLocators.LOGIN_USERNAME
            ).send_keys(username)
        with allure.step(title="Проверка наличия поля ввода пароля и ввод данных"):
            self.is_element_visible(
                *LoginPageLocators.LOGIN_PASSWORD
            ).send_keys(password)

    @allure.step(title="Авторизация пользователя")
    def authorize_guest(self, username: str, password: str):
        self.__fill_credentials_for_authorize(username, password)
        self.is_element_clickable(*LoginPageLocators.LOGIN_BUTTON). \
            click()

    def __error_message(self):
        return self.is_element_visible(*LoginPageLocators.LOGIN_ERROR_MESSAGE)

    @allure.step(title="Проверка на наличие ошибки о том, что поле 'логин' пустое")
    def should_be_username_is_required_error_message(self):
        assert self.__epic_sadface_error_messages[0] in self.__error_message().text

    @allure.step(title="Проверка на наличие ошибки о том, что поле 'пароль' пустое")
    def should_be_password_is_required_error_message(self):
        assert self.__epic_sadface_error_messages[1] in self.__error_message().text

    @allure.step(title="Проверка на наличие ошибки о том,"
                       "что заданной комбинации 'логин-пароль' не существует"
                 )
    def should_be_username_and_password_doesnt_match_error_message(self):
        assert self.__epic_sadface_error_messages[2] in self.__error_message().text
