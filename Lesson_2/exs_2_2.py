# Вывод строки в заданном формате.
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия
# lenai65209@rambler.ru

my_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_lst = []
sign = None
my_str = ""
for elem in my_lst:
    if str('+') in elem[0]:
        param = elem[1:]
        sign = '+'
    elif str('-') in elem[0]:
        sign = '+'
        param = elem[1:]
    else:
        param = elem
    try:
        param = int(param)
        if sign:
            new_lst.append('"')
            new_lst.append(f'{sign}{param:02d}')
            new_lst.append('"')
        else:
            new_lst.append('"')
            new_lst.append(f'{param:02d}')
            new_lst.append('"')
    except ValueError:
        new_lst.append(param)
print('new_lst: ', new_lst)
i = 0
while i != len(new_lst):
    if str('"') not in new_lst[i]:
        my_str += new_lst[i] + ' '
        i += 1
    else:
        my_str += '"' + new_lst[i + 1] + '"' + ' '
        i += 3
print('my_str: ', my_str)
