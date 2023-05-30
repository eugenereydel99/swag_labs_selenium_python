import allure
import pytest

from utils.constants import Urls
from pages.products_page import ProductsPage
from pages.login_page import LoginPage


@allure.severity(allure.severity_level.CRITICAL)
class TestLoginForm:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        driver.delete_all_cookies()

    @pytest.mark.negative
    @allure.title(
        test_title="Поле 'логин' пустое и поле 'пароль' пустое"
    )
    def test_login_is_empty_and_password_is_empty(self, driver):
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(username="", password="")
        login_page.should_be_username_is_required_error_message()

    @pytest.mark.negative
    @allure.title(
        test_title="Поле 'логин' пустое и поле 'пароль' валидное заполненное"
    )
    def test_login_is_empty_and_password_is_valid(self, driver):
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(
            username="",
            password=LoginPage.accepted_password
        )
        login_page.should_be_username_is_required_error_message()

    @pytest.mark.negative
    @allure.title(
        test_title="Поле 'логин' пустое и поле 'пароль' невалидное заполненное"
    )
    def test_login_is_empty_and_password_is_invalid(self, driver, faker):
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(
            username="",
            password=faker.password()
        )
        login_page.should_be_username_is_required_error_message()

    @pytest.mark.negative
    @allure.title(
        test_title="Поле 'логин' валидное заполненное и поле 'пароль' невалидное заполненное"
    )
    def test_login_is_valid_and_password_is_invalid(self, driver, faker):
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(
            username=LoginPage.accepted_usernames,
            password=faker.password()
        )
        login_page.should_be_username_and_password_doesnt_match_error_message()

    @pytest.mark.negative
    @allure.title(
        test_title="Поле 'логин' валидное заполненное и поле 'пароль' пустое"
    )
    def test_login_is_valid_and_password_is_empty(self, driver):
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(
            username=LoginPage.accepted_usernames,
            password=""
        )
        login_page.should_be_password_is_required_error_message()

    @pytest.mark.negative
    @allure.title(
        test_title="Поле 'логин' невалидное заполненное и поле 'пароль' невалидное заполненное"
    )
    def test_login_is_invalid_and_password_is_invalid(self, driver, faker):
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(
            username=faker.email(),
            password=faker.password()
        )
        login_page.should_be_username_and_password_doesnt_match_error_message()

    @pytest.mark.negative
    @allure.title(
        test_title="Поле 'логин' невалидное заполненное и поле 'пароль' пустое"
    )
    def test_login_is_invalid_and_password_is_empty(self, driver, faker):
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(
            username=faker.email(),
            password=""
        )
        login_page.should_be_password_is_required_error_message()

    @pytest.mark.negative
    @allure.title(
        test_title="Поле 'логин' невалидное заполненное и поле 'пароль' валидное заполненное"
    )
    def test_login_is_invalid_and_password_is_valid(self, driver, faker):
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(
            username=faker.email(),
            password=LoginPage.accepted_password
        )
        login_page.should_be_username_and_password_doesnt_match_error_message()

    @pytest.mark.positive
    @allure.title(
        test_title="Поле 'логин' валидное заполненное и поле 'пароль' валидное заполненное"
    )
    def test_login_is_valid_and_password_is_valid(self, driver):
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(
            username=LoginPage.accepted_usernames,
            password=LoginPage.accepted_password
        )
        products_page = ProductsPage(driver=driver, url=Urls.PRODUCTS_PAGE_URL)
        products_page.should_be_products_page()
