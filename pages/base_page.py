import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(url=self.url)

    def is_element_visible(self, how, what) -> WebElement:
        return wait(self.driver, 10).until(
            ec.visibility_of_element_located((how, what))
        )

    def are_elements_visible(self, how, what) -> WebElement:
        return wait(self.driver, 10).until(
            ec.visibility_of_all_elements_located((how, what))
        )

    def are_elements_present(self, how, what) -> WebElement:
        return wait(self.driver, 10).until(
            ec.presence_of_all_elements_located((how, what))
        )

    def is_element_clickable(self, how, what) -> WebElement:
        return wait(self.driver, 10).until(
            ec.element_to_be_clickable((how, what))

        )

    def is_element_not_visible(self, how, what) -> WebElement:
        return wait(self.driver, 10).until(
            ec.invisibility_of_element_located((how, what))
        )

    def go_to_element(self, how, what) -> None:
        iframe = self.driver.find_element((how, what))
        ActionChains(self.driver). \
            scroll_to_element(iframe). \
            perform()
