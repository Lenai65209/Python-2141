# Работа со списком.
# 2022 Елена Иконникова, Каргополь, Архангельская область, Россия
# lenai65209@rambler.ru

prices = [57.8, 46.51, 97.05, 25.6, 46.78, 81, 65.5, 11, 89, 5, 41.4, 61.18, 0.5, 28.1, 50, 16.80, 20.15, 4, 200,
          100.01, 1]
price_str = ''
for price in prices:
    price_lst = str(price).split(".")
    try:
        if price_lst[1]:
            if len(price_lst[1]) == 2:
                price_str += f"{price_lst[0]} руб {price_lst[1]} коп, "
            else:
                price_str += f"{price_lst[0]} руб {price_lst[1]}0 коп, "
    except IndexError:
        price_str += f"{price_lst[0]} руб, 00 коп, "
print(price_str[:len(price_str) - 2])
print('prices: ', prices)
print(id(prices))
prices.sort()
print('prices: ', prices)
print(id(prices))
prices_sort_new = sorted(prices, reverse=True)
print('prices_sort_new', prices_sort_new)
print(id(prices_sort_new))
print("The five most expensive: ", prices[-6:-1])
