import pytest
import time
import requests
from TrelloPages import TrelloHelper, TrelloLocators

# Variables for api requests in trello.
trello_url_get_cards = "https://api.trello.com/1/boards/vvGb4Zeh/cards"
query = {
    'key': 'YOUR_KEY',
    'token': 'YOUR_TOKEN'
}


# Функция получающая список карточек, доски Trello, по указанному Url. И возвращающая его.
def get_cards_from_trello():
    response = requests.request(
        "GET",
        trello_url_get_cards,
        params=query
    )
    # print(response.text)
    return response.text


# Фикстура создающая объект страницы 'TrelloHelper', для передачи его во все тесты.
@pytest.fixture(scope="class")
def trello_page(browser):
    trello_page = TrelloHelper(browser)
    return trello_page


# Класс с тестовыми методами, проверяющими частичный функционал в Trello.
@pytest.mark.webtest
class TestTrello:

    # Авторизация в Trello.
    def test_login_trello(self, trello_page):
        trello_page.go_to_site()
        print("Авторизуемся двойной авторизацией в Trello. \n")
        trello_page.click_on_the_come()
        trello_page.enter_login_step1("just8@mail.ru")
        trello_page.click_on_the_login_button()
        time.sleep(3)
        trello_page.enter_login_step2("silny_parol_bitbacket")
        trello_page.click_on_the_login_submit()
        time.sleep(3)
        if trello_page.is_visible('class_name', TrelloLocators.LOCATOR_Trello_LINK_AVATAR_CLASS_NAME, 'Avatar on home page '
                                                                                               'Trello') is not None:
            title = trello_page.get_title_page()
        assert "Доски" in title
        print("Проверяем, что авторизовались. И тайтл страницы содержит слово - Доски. \n")
        time.sleep(3)

    # Добавление новой карточки, в список.
    def test_add_card(self, trello_page):
        print("Выбираем тестовую доску 'test_parascript', для добавления в нее новой карточки. \n")
        trello_page.click_on_the_board_parascript()
        time.sleep(3)
        print("Добавляем новую карточку 'Test card parascript', в список. \n")
        trello_page.click_on_the_menu_cards()
        time.sleep(3)
        trello_page.click_on_the_link_add_card()
        time.sleep(3)
        trello_page.add_card("Test card parascript")
        time.sleep(3)

        print("Через api Trello проверяем, что карточка 'Test card parascript' была действительно добавлена в список.")
        list_cards_parascript = get_cards_from_trello()
        # Ищем в полученном списке карточек, добавленную карточку "Test card parascript".
        assert "Test card parascript" in list_cards_parascript
        print("Проверка assert прошла без ошибок, на наличие карточки 'Test card parascript' в списке.")

    # Перемещение добавленной карточки 'Test card parascript', в соседний список - "В процессе".
    def test_move_card(self, trello_page):
        print("Перемещаем карточку 'Test card parascript', в соседний список - 'В процессе'. \n")
        trello_page.view_card()
        time.sleep(3)
        trello_page.click_on_the_button_move()
        time.sleep(3)
        trello_page.choice_in_select_lists_in_process()
        time.sleep(3)
        trello_page.click_on_button_moved()
        time.sleep(3)
        trello_page.click_on_the_close_view_card()
        time.sleep(5)

        print("Через api Trello проверяем, что карточка 'Test card parascript' была перемещена в соседний список - 'В "
              "процессе'.")
        list_cards_parascript = get_cards_from_trello()
        # Убеждаемся, что id списка к которому принадлежит карточка, поменялся с "60e60a53b9ed7b5fcdfcdd34"("Нужно
        # сделать") на "60e60a53b9ed7b5fcdfcdd35"("В процессе"). И он присутствует в response.text.
        assert "60e60a53b9ed7b5fcdfcdd35" in list_cards_parascript
        print("Проверка assert прошла без ошибок. Значит карточка 'Test card parascript', была перемещена в список 'В "
              "процессе'.")

    # Удаление указанной карточки из списка.
    def test_delete_card(self, trello_page):
        print("Удаляем карточку 'Test card parascript' из списка. \n")
        trello_page.view_card()
        time.sleep(3)
        trello_page.delete_card()
        time.sleep(3)

        print("Через api Trello проверяем, что карточка 'Test card parascript' была действительно удалена из списка.")
        list_cards_parascript = get_cards_from_trello()
        assert "Test card parascript" not in list_cards_parascript
        print("Проверка assert прошла без ошибок, на отсутствие карточки 'Test card parascript' в списке.")

    # Разлогинивание из аккаунта Trello.
    def test_logout_trello(self, trello_page):
        print("Выходим, двойным выходом, из аккаунта Trello. \n")
        trello_page.click_on_the_avatar()
        time.sleep(5)
        trello_page.click_on_the_link_logout()
        time.sleep(3)
        trello_page.click_on_the_button_logout()
        time.sleep(3)
        title = trello_page.get_title_page()
        assert "Вы не авторизованы" in title
        assert title == "Вы не авторизованы в Trello"
        print("Проверяем, что вышли из аккаунта Trello. И тайтл страницы содержит фразу - Вы не авторизованы в "
              "Trello. \n")
        time.sleep(3)
