Данный автотест на pytest, проверяет несколько базовых функций Trello: 
 1. Двойная авторизация в Трелло. 
 2. Выбор указанной доски, и добавление на нее новой карточки. 
 3. Перемещение новой добавленной карточки, в соседний список. 
 4. Удаление добавленной карточки. 
 5. Разлогинивание и выход из аккаунта Трелло. 
 
По всем указанным действиям добавленны assert, проверки. 
К пунктам по добавлению, перемещению и удалению карточки, проверки производятся через api запрос. 
Т.е. выполняется запрос, на получение списка карточек, указанной доски. И в response ищется необходимая информация, по каждой из проверок.     

This autotest on pytest, checks several basic Trello functions:

1. Dual Authorization in Trello.
2. Selecting the specified board, and adding a new card to it.
3. Moving the newly added card, to the adjacent list.
4. Deleting the added card.
5. Logging out of the Trello account.

For all of these actions added Assert, checks. To items on: Adding, Moving and Deleting the card, the checks are made through api request. I.e., a request for a list of cards of the specified board is executed. And in Response the necessary information is searched for each of the checks.
  

# Installation


Installing dependencies:

    pip install -r requirements.txt
    pip install allure-pytest
    

# Running the test
    pytest -v TestTrello.py --alluredir reports/allure


## View reports in allure
    allure serve reports/allure

Learn more about how to configure allure - https://github.com/allure-framework/allure2



Link to the demo of this AutoTest - https://drive.google.com/file/d/1F5KRLla2fA_S04UpGmmr3QpkZPMYs8gN/view?usp=sharing

