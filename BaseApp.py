from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List


# Создаем класс BasePage, с базовыми методами, для работы с WebDriver.
class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.base_url = "https://trello.com/"
        self.__wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(EC.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(EC.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_page_text(self):
        return self.driver.page_source
