# Список, состоящий из кубов нечётных чисел от 1 до 1000.
# Суммф тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# К каждому элементу списка добавить 17
# Заново вычислиена сумма тех чисел из этого (нового) списка, сумма цифр которых делится нацело на 7
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия
# lenai65209@rambler.ru


my_num = [num ** 3 for num in range(1, 1000) if num % 2]
print("numbers", my_num)
my_sam = 0


def my_ten(my_num_lst):
    num_lst = []
    result = 0
    num_lst.append(my_num_lst % 10)
    while my_num_lst // 10:
        my_num_lst = my_num_lst // 10
        num_lst.append(my_num_lst % 10)
    for figure in num_lst:
        result += figure
    if result % 7 == 0:
        return result
    else:
        return 0


for num in my_num:
    if my_ten(num):
        my_sam += num
print('my_sam', my_sam)

my_sam = 0
for num in my_num:
    num = num + 17
    if my_ten(num):
        my_sam += num  # не совсем ясно надо ли убирать 17 (my_sam += nam - 17)
print('my_sam', my_sam)

my_sam = 0
for num in my_num:
    num = num + 17
    if my_ten(num):
        my_sam += num - 17
print('my_sam', my_sam)
