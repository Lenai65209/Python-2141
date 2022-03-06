#  Функция, email_parse(<email_address>),
#  которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
#  и возвращает их в виде словаря.
#  Если адрес не валиден, выбросывает исключение ValueError.
#  скрипт exs_7_5.py находится в папке venv, откуда его и запускали.

import re
from sys import argv


def email_parse(email_address):
    """
    checks email validity

   :param email_address: email address
   :return email address or raise ValueError
    """
    NOT_IN_EMAIL = re.compile(r'\s|:|;|\!|#|%|\*|\(|\)|=|\+|\{|\}|\[|\]|\\|/|\|')  # символы которых не должно быть.
    RE_EMAIL = re.compile(r'[^\.][(a-z0-9\.){1,}]{4,}[^\.]\@[(a-z0-9\.){1,}]{2,}\.[a-z]{2,4}',
                          re.IGNORECASE)  # возможно, не все правильно. Смотрела здесь: https://htmlweb.ru/java/example/test_e-mail.php
    RE_EMAIL_2 = re.compile(r'\.{2,}', re.IGNORECASE)  # две точки рядом.
    # RE_GET_PARSER = re.compile(r'(?<=^)(?P<key>[^&]+)\@(?P<val>([^\.]+)){1,}') # точка может быть не одна. Можно ли написать неизвестное количество <val>7
    dic_email = {}
    my_re_mail_2 = RE_EMAIL_2.findall(email_address)
    my_re_mail = RE_EMAIL.findall(email_address)
    not_in_my_mail = NOT_IN_EMAIL.findall(email_address)
    if len(my_re_mail) == 1 and len(email_address) == len(my_re_mail[0]) and len(not_in_my_mail) == 0 and len(
            my_re_mail_2) == 0:
        # try:
        #     print(*map(lambda x: x.groupdict(), RE_GET_PARSER.finditer(email_address)), sep=', ') # распечатаем словарь для адреса с одной точкой после @.
        # except:
        #     pass
        cop_email_address = re.split('@', email_address)
        sp_cop_email_address_1 = re.split('\.+', cop_email_address[1])
        sp_cop_email_address_1.pop()
        key_email_address = cop_email_address[0]
        dic_email[key_email_address] = sp_cop_email_address_1
        return dic_email
    else:
        msg = f'wrong email:{email_address}'
        raise ValueError(msg)


if __name__ == '__main__':
    my_email_address = argv[1]  # email адрес.
    res = email_parse(my_email_address)
    print(f"Вернули словарь: {res}.")
    for key in res.keys():
        print(f"Имя пользователя {key}")
    print("Почтовые домены: ")
    for val in res[key]:
        print(f'- {val}')

# john13456@example.com валидный
# john.smith@example.com валидный
# john.smith@exam.ple.com валидный
# John..Doe@example.com не валидный
# .Doe@example.com не валидный
# John.@example.com не валидный
# john.smithexam.ple.com не валидный
# john.smith@example не валидный
