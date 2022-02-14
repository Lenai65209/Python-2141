from exs_4_2 import currency_rates

valute_name = input("Введите код валюты, чтобы узнать курс: ")
answer = currency_rates(valute_name)
print(f'Курс {valute_name}: {answer[0]}, {answer[1]}')
dollar_exchange_rate = currency_rates("USD")
print(f'Курс доллара: {dollar_exchange_rate[0]}, {dollar_exchange_rate[1]}')
euro_exchange_rate = currency_rates("EUR")
print(f'Курс евро: {euro_exchange_rate[0]}, {euro_exchange_rate[1]}')
GBP_exchange_rate = currency_rates("GBP")
print(f'Курс Британского фунта стерлингов: {GBP_exchange_rate[0]}, {GBP_exchange_rate[1]}')
