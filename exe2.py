import json

from requests import get


class MyError(Exception):
    '''Данные не получены'''
    pass


def currency_rates(valute_name):
    '''returns the currency exchange rate and the date of the exchange rate by code'''
    try:
        response = get('https://www.cbr-xml-daily.ru/daily_json.js')
        response.encoding = 'utf-8'
        json_data = json.loads(response.text)
        if valute_name in json_data['Valute']:
            dic_valute = json_data['Valute'][valute_name]
            data = json_data['Date'][0:10]
            return dic_valute['Value'], data
        else:
            return ('К сожадению', "такой валюты нет")
    except:
        raise MyError("Данные о валютах не получены")


if __name__ == '__main__':
    valute_name = input("Введите код валюты, чтобы узнать курс: ")
    answer = currency_rates(valute_name)
    print(f'Курс {valute_name}: {answer[0]}, {answer[1]}')
    dollar_exchange_rate = currency_rates("USD")
    print(f'Курс доллара: {dollar_exchange_rate[0]}, {dollar_exchange_rate[1]}')
    euro_exchange_rate = currency_rates("EUR")
    print(f'Курс евро: {euro_exchange_rate[0]}, {euro_exchange_rate[1]}')
