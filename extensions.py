import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass


class APIException:
    @staticmethod
    def convert(quote: str, base: str, amount: str ):
        if quote == base:
            raise ConvertionExeption(f'Невозможно конвертировать одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        get_price = json.loads(r.content)[keys[base]]

        return get_price
