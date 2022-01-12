import os

import allure
import pytest
from selenium import webdriver

from utils import *

from datetime import datetime

timestamp = datetime.now().strftime('%H-%M-%S')


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # Открываем браузер во весь экран.
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Используем конструкцию yield, которая разделяет функцию browser() на часть — до тестов и после тестов.
    yield driver
    driver.quit()


# Хук, для создания скриншотов страницы, при падении тестов. И для отправления описания тестов, в отчет.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Добавление описания теста, в отчет. Берется из комментария к тесту.
    test_fn = item.obj
    # Получаем описание теста, из комментария к нему.
    docstring = getattr(test_fn, '__doc__')
    # Получаем название теста.
    nametest = getattr(test_fn, '__name__')
    if docstring:
        rep.nodeid = docstring

    # Cоздание скриншотов страницы, при падении тестов.
    # Для добавления одного из них в allure-отчет и второго, для отправления его в slack.
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return

            # Формируем скриншот, для allure-отчета.
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )

            # Создаем скриншот страницы, где произошло падение теста, для слака.
            web_driver.save_screenshot('screen_page_when_failure' + timestamp + '.png')

            # Функционал отправления скриншота страницы, где произошло падение теста с описанием, в слак.
            # Получаем информацию о падениях теста.
            excinfo = call.excinfo
            # longrepr = excinfo
            r = excinfo._getreprcrash()  # получаем общую информацию об ошибке.
            longrepr = (r.path, r.lineno, r.message)  # разделяем ее на отдельные части: путь к файлу с ошибкой,
            # линия в файле, на которой произошла ошибка и описание ошибки.

            # Формируем общую переменную, с текстом, для отправления его в слак.
            message_slack = f'В тесте - "{docstring}", произошла ошибка. \n Ее описание: {longrepr}'
            # Отправляем сообщение со скриншотом, в слак, функцией send_message. Ее описание находится в файле utils.py.
            send_message('screen_page_when_failure' + timestamp + '.png',
                         message_slack)
            # Удаление созданного скриншота для слака, из папки с тестовым фреймворком, после отправления скрина в слак.
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                'screen_page_when_failure' + timestamp + '.png')
            os.remove(path)

        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
