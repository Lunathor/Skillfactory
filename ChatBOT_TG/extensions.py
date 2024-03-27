import requests
import json
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        if quote not in keys or base not in keys:
            raise APIException(f"Валюты нет в списке валют (ПРОВЕРЬТЕ ПРАВИЛЬНОСТЬ НАПИСАНИЯ НАЗВАНИЯ ВАЛЮТЫ)")
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}")
        
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}")
        
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        
        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/db94d74c500fd07650adcd84/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)['conversion_rate']
        return total_base * amount

