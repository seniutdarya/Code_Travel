#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import get
import sms
import music
import validate
import install
from pathlib import Path

install.install_lib("colorama")
from colorama import init, Fore, Back, Style
init(autoreset=True)


THEMES_PATH = "./themes"
COUNT_QUESTIONS = 10


def choice_them(list_themes):
    them = None
    not_break = True
    while not_break:
        choice = input("Пожалуйста, выбирайте тему 1, 2 и т.д: ")
        for them in list_themes:
            if f"{choice}." in them:
                not_break = False
                break
        else:
            print("Некорректный выбор")
            music.uncorrect()

    return them


def print_return_themes(list_themes):
    list_themes.sort()
    print(*[Path(f).stem for f in list_themes if f != "__pycache__"], sep='\n')
    return list_themes


def write_result(*args):
    with open("result.txt", "w", encoding="utf-8") as result:
        for i in args:
            if isinstance(i, list):
                for e in i:
                    result.write(f"{e}\n")
            else:
                result.write(f"{i}\n")


def quiz(them):
    answers = []
    correct_answers_count = 0

    install.install_lib("pandas")
    import pandas as pd
    # data frame
    df = pd.read_csv(f"{THEMES_PATH}/{them}", delimiter=";", dtype=str)\
        .sample(frac=1)\
        .reset_index(drop=True)\
        .head(COUNT_QUESTIONS)

    for idx in df.index:
        _question = df['question'][idx]
        _variant = df['variant'][idx]
        _answer = df['answer'][idx]
        print(_question, _variant, sep='\n')
        answer = validate.handle_answer()
        # сравниваем ответы
        if answer == _answer:
            print(Fore.GREEN + f'{answer} - Отлично\n')
            correct_answers_count += 1
            music.correct()
        else:
            print(Fore.RED + f'{answer} - К сожалению нет\n', end='\n')
            music.fal()

        answers.append(f"{_question}\n{_variant}\nВаш ответ: {answer}\nПравильный ответ: {_answer}")
    return correct_answers_count, answers


def add_result():
    with open("full_result.txt", "a", encoding="utf-8") as full_result:
        with open("result.txt", "r", encoding="utf-8") as res:
            for r in res:
                full_result.write(r)
            full_result.write("-------------------------------------------------------------------------------------\n")


def add_client(*args):
    with open("clients.txt", "a", encoding="utf-8") as f:
        for e in args:
            f.write(f"{e}\n")
        f.write("---------------------------------------------------------------------------------------\n")


def convert_result(*args):
    install.install_lib('FPDF')
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('Arial', '', r"./arial/arial.ttf", uni=True)
    pdf.set_font('Arial', '', 14)
    for l in args:
        if isinstance(l,str):
            pdf.multi_cell(200, 10, l, align="L")
        elif isinstance(l,list):
            for s in l:
                pdf.multi_cell(200, 10, s, align="L")
    pdf.output("result.pdf")


def send_email(is_send, mail):
    if is_send.upper() == "ДА":
        from send_email import _send_mail
        _send_mail(mail, mail, "Discount", "Результаты", "./result.pdf")


def main():
    name = get.get_name()

    init = f"\n    {name}, pады приветствовать Вас на нашей страничке.\n" \
           f"    Предлагаем отправиться в увлекательное путешествие от ЛаймТур в любые уголки света.\n" \
           f"    Пройди мини-викторину из 10 вопросов и получи бонус в виде 10% скидки на пакетные туры в Египет, Турцию и Испанию.\n"
    print(init)


    print("Наша мини-викторина предоставляет Вам тему на выбор:")
    list_themes = print_return_themes(get.get_themes(THEMES_PATH))
    them = choice_them(list_themes)
    correct_answers_count, answers = quiz(them)
    percent = get.get_percent(correct_answers_count)
    disc = get.get_discount(percent)

    print(Style.BRIGHT+f" ***Поздравляем!***\n", Style.BRIGHT+Back.BLUE+f"Ваша скидка - {disc}%. "+ Style.RESET_ALL,"\n"
          f"\nДля того, чтобы получить консультацию как воспользоваться скидкой,\n"
          f"заполните, пожалуйста, следующую информацию и наш менеджер свяжется с Вами по удобному каналу связи.\n")
    music.win()
    phone_number = get.get_phone()
    mail = get.get_email()
    # Запись результатов в файл
    write_result(f"Имя: {name}",
                 f"Телефон: {phone_number}",
                 answers,
                 f"Ваша скидка: {disc}%")

    add_client(name, phone_number, mail)

    print(f"\nВаш результат в txt: {os.path.dirname(__file__)}")

    add_result()
    convert_result(f"Имя: {name}", f"Телефон: {phone_number}", answers, f"Ваша скидка: {disc}%")

    is_send = input("Хотите получить результат на почту?: ")
    send_email(is_send, mail)

    sms.send_sms(phone_number, mail, name)

    print("\nСпасибо за прохождение викторины,доброго дня!")


if __name__ == "__main__":
    main()
