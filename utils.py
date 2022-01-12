import json
import logging

import requests

from slackclient import SlackClient

from jenkinsapi.jenkins import Jenkins

logger = logging.getLogger(__name__)

# Токен для работы со слак-ботом.
slack_token_bot = 'YOUR_TOKEN'
slack_client = SlackClient('YOUR_TOKEN')


# Данная функция отправляет сообщение в слак, вместе с прикрепленной картинкой.
def send_message(file, initial_comment, job_channel="for_autotests"):
    r = requests.post('https://slack.com/api/files.upload',
                      data={'token': slack_token_bot,
                            'channels': [job_channel], 'as_user': True,
                            'title': 'Скрин страницы, где произошла ошибка', 'initial_comment': initial_comment},
                      files={'file': open(file, 'rb')})


# Данная функция отправляет сообщение в слак, без картинки. В указанный в аргументе job_channel, слак канал.
def send_message_no_file(msg, job_channel="for_autotests"):
    slack_client.api_call(
        "chat.postMessage",
        channel=job_channel,
        text=msg,
        username='bot_autotests',
        icon_emoji=':robot_face:'
    )


# Данная функция  формирует текст с ошибками, для отправления его в чат ботом. Также данная функция будет пересылать
# файл в send_message(), для отправки его в чат. В слак-канал, указанный в переменной job_channel.
def message_text_formation(index, msg, url_err, screenshot, job_channel):
    message_slack = f'Ошибка №{str(index)}. Подробное описание: \n URL страницы, где произошла ошибка: {url_err} \n Текст ошибки: {msg}'

    # Вызываем функцию, отправляющую сообщения в чат.
    send_message(screenshot, message_slack, job_channel)


# Данная функция работает с api Jenkins. Отправляет ссылку на allure-отчетность в слак, по тому автотесту,
# который был запущен в Дженкинс.
def getDataAboutChoiceJob(url, job_way, job_name, job_channel, username=None, password=None):
    J = Jenkins(url, username, password)
    job = J[job_name]

    job_name_allure = J[job_name].name
    job_way_autotest = job_way
    build_last = job.get_last_build()
    build_last_str = str(build_last)
    build_last_int = build_last_str[len(build_last_str) - 1]

    # Заполняем переменную с сообщением, для отправления ее в слак. url_allure = f"Ссылка на allure-отчет в Дженкинсе
    # - http://51.68.87.5:8080/view/Functional_autotests/job/{job_way_autotest}/{build_last_int}/allure/." \ f"\n По
    # автотесту - {job_name_allure}."

    # Данные для prod-jenkins:
    url_allure = f"Ссылка на allure-отчет в Дженкинсе - http://51.68.87.5:8080/view/Functional_autotests/job/{job_way_autotest}/allure/." \
                 f"\n По автотесту - {job_name_allure}."
    # Данные для dev-jenkins:
    # url_allure = f"Ссылка на allure-отчет в Дженкинсе - http://192.168.1.172:8080/job/{job_way_autotest}/allure/." \
    #                   f"\n По автотесту - {job_name_allure}."

    # Вызываем функцию, отправляющую сообщения в чат.
    send_message_no_file(url_allure, job_channel)

