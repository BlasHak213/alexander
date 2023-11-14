import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Укажите разные типы валют для конвертации')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Укажите верное название валюты {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Укажите верное название валюты {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Укажите корректную сумму перевода {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base