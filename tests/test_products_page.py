import allure
import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.constants import SortingType
from utils.constants import Urls


class TestProductsPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        driver.delete_all_cookies()
        login_page = LoginPage(driver=driver, url=Urls.LOGIN_PAGE_URL)
        login_page.open()
        login_page.authorize_guest(
            username=LoginPage.accepted_usernames,
            password=LoginPage.accepted_password
        )

    @allure.title(test_title="Пользователь может отфильтровать список товаров на странице")
    @pytest.mark.parametrize(
        "sort_type",
        [
            SortingType.ALPHABETICAL_ORDER_BY_ASC,
            SortingType.ALPHABETICAL_ORDER_BY_DESC,
            SortingType.PRICE_ORDER_BY_ASC,
            SortingType.PRICE_ORDER_BY_DESC
        ]
    )
    def test_user_can_filter_list_of_products(self, driver, sort_type):
        products_page = ProductsPage(driver=driver, url=Urls.PRODUCTS_PAGE_URL)
        products_page.open()
        products_page.sort_list_of_products(sort_type=sort_type)

    @allure.title(test_title="Пользователь может добавить товар в корзину")
    @pytest.mark.skip(reason="Не реализовано")
    def test_user_can_add_product_to_card(self, driver):
        products_page = ProductsPage(driver=driver, url=Urls.PRODUCTS_PAGE_URL)
        products_page.open()
        products_page.add_products_to_cart()
        products_page.check_added_products_to_cart()
