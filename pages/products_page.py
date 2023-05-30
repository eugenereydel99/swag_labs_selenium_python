import allure

from pages.base_page import BasePage
from utils.locators import ProductsPageLocators


class ProductsPage(BasePage):
    @allure.step(title="Проверка нахождения на странице с товарами")
    def should_be_products_page(self):
        self.__should_be_products_page_link()
        self.__should_be_products_title()
        self.__should_be_products_list()

    @allure.step(title="Проверка нахождения в поисковой строке html-страницы с товарами")
    def __should_be_products_page_link(self):
        assert "inventory.html" in self.driver.current_url

    @allure.step(title="Проверка наличия заголовка 'Products'")
    def __should_be_products_title(self):
        assert "Products" in self.is_element_visible(
            *ProductsPageLocators.PRODUCTS_TITLE
        ).text

    @allure.step(title="Проверка наличия списка товаров")
    def __should_be_products_list(self):
        # Придумать ещё, что проверить на этой странице, чтобы
        # убедиться что действительно список товаров присутствует)
        assert self.is_element_visible(*ProductsPageLocators.PRODUCTS_LIST)
