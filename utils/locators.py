from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LOGO = (By.XPATH, "//div[@class='login_logo' and text()='Swag Labs']")
    LOGIN_FORM = (By.CLASS_NAME, "login-box")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "input[data-test='username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[data-test='login-button']")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")


class ProductsPageLocators:
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    PRODUCTS_LIST = (By.CLASS_NAME, "inventory_list")
    PRODUCTS_ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(@data-test, 'add-to-cart')]")
    PRODUCTS_REMOVE_FROM_CART_BUTTONS = (By.XPATH, "//button[contains(@data-test, 'remove')]")

    # Для сортировки
    PRODUCTS_LIST_FILTER = (By.CSS_SELECTOR, "select.product_sort_container")
    PRODUCTS_LIST_TITLE = (By.CSS_SELECTOR, ".inventory_list .inventory_item_name")
    PRODUCTS_LIST_PRICE = (By.CSS_SELECTOR, ".inventory_list .inventory_item_price")

    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
