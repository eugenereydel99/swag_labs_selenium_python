from enum import Enum

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
              "Chrome/110.0.0.0 YaBrowser/23.3.4.603 Yowser/2.5 Safari/537.36"


class Urls:
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"


class SortingType(Enum):
    ALPHABETICAL_ORDER_BY_ASC = "az"
    ALPHABETICAL_ORDER_BY_DESC = "za"
    PRICE_ORDER_BY_ASC = "lohi"
    PRICE_ORDER_BY_DESC = "hilo"
