import re

import music


def valid_number(phone_number):
    if len(phone_number) != 12:
        return False
    for i in range(12):
        if i in [2, 6, 9]:
            if phone_number[i] != '-':
                return False
        elif not phone_number[i].isnumeric():
            return False
    return True


def handle_answer():
    while True:
        answer = input("Введите ответ 1 или 2 и т.д.: ")
        if answer.isnumeric():
            return answer
        else:
            print("Некорректный вариант")
            music.uncorrect()


def check_email(email):
    # pass the regular expression and the email into the fullmatch() method
    # patern
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        print("Email принят")
        return True
    else:
        print("Некорректный Email")
        music.uncorrect()
        return False

