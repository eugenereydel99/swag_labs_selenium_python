import allure
import pytest

from utils.constants import Urls
from utils.locators import SortingTypeLocators
from pages.products_page import ProductsPage
from utils.functional import get_constant_attributes_from_class


class TestProductsPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        driver.delete_all_cookies()
        driver.add_cookie(
            {
                "session-username": "standard_user",
                "domain": "www.saucedemo.com",
                "path": "/",
                "expiry": "2023-06-28T00:00:00.000Z"
            }
        )

    @allure.title(test_title="Пользователь может отфильтровать список товаров на странице")
    @pytest.mark.parametrize(
        "sort_type",
        get_constant_attributes_from_class(class_name=SortingTypeLocators)
    )
    @pytest.mark.skip(reason="Не реализовано")
    def test_user_can_filter_list_of_products(self, driver, sort_type):
        products_page = ProductsPage(driver=driver, url=Urls.PRODUCTS_PAGE_URL)
        products_page.open()
        products_page.sort_list_of_products(sort_type)

    @allure.title(test_title="Пользователь может добавить товар в корзину")
    @pytest.mark.skip(reason="Не реализовано")
    def test_user_can_add_product_to_card(self, driver):
        products_page = ProductsPage(driver=driver, url=Urls.PRODUCTS_PAGE_URL)
        products_page.open()
        products_page.add_products_to_cart()
        products_page.check_added_products_to_cart()
