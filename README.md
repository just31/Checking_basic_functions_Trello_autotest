Данный автотест на pytest, проверяет несколько базовых функций Trello: 
 1. Двойная авторизация в Трелло. 
 2. Выбор указанной доски, и добавление на нее новой карточки. 
 3. Перемещение новой добавленной карточки, в соседний список. 
 4. Удаление добавленной карточки. 
 5. Разлогинивание и выход из аккаунта Трелло. 
 
По всем указанным действиям добавленны assert, проверки. 
К пунктам по добавлению, перемещению и удалению карточки, проверки производятся через api запрос. 
Т.е. выполняется запрос, на получение списка карточек, указанной доски. И в response ищется необходимая информация, по каждой из проверок.     
  

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

