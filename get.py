import os
import json

import music
import validate
from main import COUNT_QUESTIONS


def get_themes(dir):
    return [f for f in os.listdir(dir)]


def get_percent(correct_answers_count):
    perc = (100 * correct_answers_count) // COUNT_QUESTIONS
    print(f"Процент правильных ответов: {perc}%\n")
    return perc


def get_discount(percent):
    with open("discounts.json", "r", encoding="utf-8") as f:
        disc = json.load(f)
    for k, v in disc.items():
        ll = k.split("-")
        if int(ll[0]) <= percent <= int(ll[1]):
            return v


def get_phone():
    while True:
        phone_number = input("Введите номер телефона формата ХХ-XXX-XX-XX (например 29-111-11-11): +375 ")
        if validate.valid_number(phone_number):
            print("Телефон принят")
            break
        else:
            print("Некорректный номер телефона")
            music.uncorrect()
    return f"+375-{phone_number}"


def get_email():
    while True:
        mail = input("Введите e-mail: ")
        if validate.check_email(mail):
            break
    return mail


def get_name():
    music.hello()
    while True:
        name = input("Представтесь пожалуйста: ").title()
        if name.isalpha():
            break
        else:
            print("Некорректное имя")
            music.uncorrect()
    return name
