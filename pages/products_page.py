import random

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from utils.constants import SortingType
from utils.locators import ProductsPageLocators


class ProductsPage(BasePage):
    @allure.step(title="Добавление товаров в корзину")
    def add_products_to_cart(self):
        self.should_be_products_page()
        # получаем список товаров (кнопок 'Добавить')
        products_list: list[WebElement] = self.are_elements_visible(
            *ProductsPageLocators.PRODUCTS_ADD_TO_CART_BUTTONS
        )

        random_products: list[WebElement] = random.choices(
            products_list,
            k=random.choice(
                [i for i in range(1, len(products_list))]
            )
        )

        print(f"Количество выбранных товаров: {len(random_products)}")
        for product in random_products:
            product.click()

        with allure.step(title="Проверка количества добавленных товаров через бадж у значка 'Корзина'"):
            # проверяем, что количество товаров в бадже такое же, сколько товаров было кликнуто
            added_products_buttons = len(self.are_elements_visible(
                *ProductsPageLocators.PRODUCTS_REMOVE_FROM_CART_BUTTONS
            ))
            products_quantity_in_badge = int(self.is_element_visible(
                *ProductsPageLocators.SHOPPING_CART_BADGE
            ).text)

            assert added_products_buttons == products_quantity_in_badge

    @allure.step(title="Представление товаров в зависимости от типа сортировки")
    def sort_list_of_products(self, sort_type: SortingType):
        self.should_be_products_page()
        products_filter = Select(
            self.is_element_visible(*ProductsPageLocators.PRODUCTS_LIST_FILTER)
        )
        match sort_type:
            case SortingType.ALPHABETICAL_ORDER_BY_ASC as a_to_z:
                self.__select_filter_value_and_compare_lists(
                    *ProductsPageLocators.PRODUCTS_LIST_TITLE,
                    select=products_filter,
                    filter_value=a_to_z.value,
                    is_price_filter=False,
                    is_reverse=False
                )

            case SortingType.ALPHABETICAL_ORDER_BY_DESC as z_to_a:
                self.__select_filter_value_and_compare_lists(
                    *ProductsPageLocators.PRODUCTS_LIST_TITLE,
                    select=products_filter,
                    filter_value=z_to_a.value,
                    is_price_filter=False,
                    is_reverse=True
                )

            case SortingType.PRICE_ORDER_BY_ASC as low_to_high_price:
                self.__select_filter_value_and_compare_lists(
                    *ProductsPageLocators.PRODUCTS_LIST_PRICE,
                    select=products_filter,
                    filter_value=low_to_high_price.value,
                    is_price_filter=True,
                    is_reverse=False
                )

            case SortingType.ALPHABETICAL_ORDER_BY_DESC as high_to_low_price:
                self.__select_filter_value_and_compare_lists(
                    *ProductsPageLocators.PRODUCTS_LIST_PRICE,
                    select=products_filter,
                    filter_value=high_to_low_price.value,
                    is_price_filter=True,
                    is_reverse=True
                )

    @allure.step(title="Проверка нахождения на странице с товарами")
    def should_be_products_page(self):
        self.__should_be_products_page_link()
        self.__should_be_products_title()
        self.__should_be_products_list()

    def __select_filter_value_and_compare_lists(
            self,
            *locator,
            select: Select,
            filter_value: str,
            is_price_filter: bool,
            is_reverse: bool = True
    ) -> None:
        select.select_by_value(filter_value)
        if is_price_filter:
            original_list = list(
                map(lambda x: float(x.text.removeprefix('$')), self.are_elements_visible(*locator))
            )
        else:
            original_list = list(
                map(lambda x: x.text, self.are_elements_visible(*locator))
            )
        sorted_list = sorted(original_list, reverse=is_reverse)
        assert original_list == sorted_list

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
