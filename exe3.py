# Склонение процентов.
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия
# lenai65209@rambler.ru


def my_like_pers(my_pers):
    if i % 10 == 1 and i != 11:
        print(my_pers, 'процент')

    elif 2 <= i % 10 <= 4 and i != 12 and i != 13 and i != 14:
        print(my_pers, 'процента')

    else:
        print(my_pers, 'процентов')


for i in range(101):
    my_like_pers(i)
