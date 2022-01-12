from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# Реализуем класс с методами, для страницы регистрации.
class TrelloLocators:
    # Authorization
    LOCATOR_Trello_LINK_COME = (By.LINK_TEXT, "Войти")
    LOCATOR_Trello_FIELD_USER = (By.ID, "user")
    LOCATOR_Trello_FIELD_PASSWORD = (By.ID, "password")
    LOCATOR_Trello_LOGIN_BUTTON = (By.ID, "login")
    LOCATOR_Trello_LOGIN_SUBMIT = (By.ID, "login-submit")

    # Profile account
    LOCATOR_Trello_LINK_AVATAR = (By.CLASS_NAME, "_2LKdO6O3n25FhC")
    LOCATOR_Trello_LINK_AVATAR_CLASS_NAME = "_2LKdO6O3n25FhC"

    # Logout
    LOCATOR_Trello_LINK_LOGOUT = (By.XPATH, "//span[contains( text(),'Выйти')]")
    LOCATOR_Trello_LOGIN_BUTTON_LOGOUT = (By.XPATH, "//span[@class='css-19r5em7']")

    # Choice of boards
    LOCATOR_Trello_BOARD_PARASCRIPT = (By.XPATH, "//div[@title='test_parascript']")

    # Add card
    LOCATOR_Trello_MENU_CARDS = (By.XPATH, "//a[@aria-label='Действия со списком']")
    LOCATOR_Trello_ADD_CARD = (By.XPATH, "//a[contains( text(),'Добавить карточку…')]")
    LOCATOR_Trello_FIELD_NAME_BOARD = (By.XPATH, "//textarea[@placeholder='Ввести заголовок для этой карточки']")
    LOCATOR_Trello_ADD_CARD_BUTTON = (By.XPATH, "//input[@value='Добавить карточку']")

    # Move card
    LOCATOR_Trello_BUTTON_MOVE = (By.XPATH, "//span[contains( text(),'Перемещение')]")
    LOCATOR_Trello_BUTTON_MOVED = (By.XPATH, "//input[@value='Переместить']")

    # View card
    LOCATOR_Trello_VIEW_CARD = (By.XPATH, "//span[contains( text(),'Test card parascript')]")
    LOCATOR_Trello_LOGIN_BUTTON_ARCIVING_IN_VIEW = (By.XPATH, "//span[@title='Архивация']")
    LOCATOR_Trello_LOGIN_BUTTON_ARCIVING_IN_VIEW = (By.XPATH, "//span[@title='Архивация']")
    LOCATOR_Trello_CLOSE_VIEW_CARD = (By.XPATH, "//a[@class='icon-md icon-close dialog-close-button js-close-window']")
    LOCATOR_Trello_SELECT_IN_PROCESS = (By.XPATH, "//select[@class='js-select-list']/option[text()='В процессе']")

    # Delete selected card
    LOCATOR_Trello_LOGIN_BUTTON_REMOVE_ONE_IN_VIEW = (By.XPATH, "//a[@title='Удалить']")
    LOCATOR_Trello_INPUT_REMOVE_TWO_IN_VIEW = (By.XPATH, "//input[@value='Удалить']")


class TrelloHelper(BasePage):

    # Authorization
    def click_on_the_come(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_LINK_COME, time=2).click()

    def enter_login_step1(self, user):
        user_field = self.find_element(TrelloLocators.LOCATOR_Trello_FIELD_USER)
        user_field.click()
        user_field.send_keys(user)

    def enter_login_step2(self, password):
        last_name_field = self.find_element(TrelloLocators.LOCATOR_Trello_FIELD_PASSWORD)
        last_name_field.click()
        last_name_field.send_keys(password)

    def click_on_the_login_button(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_LOGIN_BUTTON, time=2).click()

    def click_on_the_login_submit(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_LOGIN_SUBMIT, time=2).click()

    # Profile
    def click_on_the_avatar(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_LINK_AVATAR, time=2).click()

    # Logout
    def click_on_the_link_logout(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_LINK_LOGOUT, time=2).click()

    def click_on_the_button_logout(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_LOGIN_BUTTON_LOGOUT, time=2).click()

    # Choice of boards
    def click_on_the_board_parascript(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_BOARD_PARASCRIPT, time=2).click()

    # Add card
    def click_on_the_menu_cards(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_MENU_CARDS, time=2).click()

    def click_on_the_link_add_card(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_ADD_CARD, time=2).click()

    def add_card(self, name_board):
        board_name_field = self.find_element(TrelloLocators.LOCATOR_Trello_FIELD_NAME_BOARD)
        board_name_field.click()
        board_name_field.send_keys(name_board)
        self.find_element(TrelloLocators.LOCATOR_Trello_ADD_CARD_BUTTON, time=2).click()

    # Move card
    def click_on_the_button_move(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_BUTTON_MOVE, time=2).click()

    def choice_in_select_lists_in_process(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_SELECT_IN_PROCESS, time=2).click()

    def click_on_button_moved(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_BUTTON_MOVED, time=2).click()

    # View card
    def view_card(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_VIEW_CARD, time=2).click()

    def click_on_the_close_view_card(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_CLOSE_VIEW_CARD, time=2).click()

    # Delete selected card
    def delete_card(self):
        self.find_element(TrelloLocators.LOCATOR_Trello_LOGIN_BUTTON_ARCIVING_IN_VIEW, time=2).click()
        time.sleep(3)
        self.find_element(TrelloLocators.LOCATOR_Trello_LOGIN_BUTTON_REMOVE_ONE_IN_VIEW, time=2).click()
        time.sleep(3)
        self.find_element(TrelloLocators.LOCATOR_Trello_INPUT_REMOVE_TWO_IN_VIEW, time=2).click()

    # Secondary functions
    def check_present_word(self):
        page_text = self.get_page_text()
        return page_text

    def get_title_page(self):
        page_title = self.driver.title
        return page_title

    def page_refresh(self):
        self.driver.refresh()
