# Перевод секунд в дни, часы, минуты и секунды.
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия
# lenai65209@rambler.ru


duration = int(input('Введите время в секундах '))
days = 0
hours = 0
minutes = 0
seconds = 0
if duration // 60:
    minutes = duration // 60
    seconds = duration % 60
    if minutes // 60:
        hours = minutes // 60
        minutes = minutes % 60
        if hours // 24:
            days = hours // 24
            hours = hours % 24
            print(days, 'dh', hours, 'hh', minutes, 'mh', seconds, 'sh')
        else:
            print(hours, 'hh1', minutes, 'mh1', seconds, 'sh1')
    else:
        print(minutes, 'mm1', seconds, 'ms1')
else:
    print('duration', duration)
