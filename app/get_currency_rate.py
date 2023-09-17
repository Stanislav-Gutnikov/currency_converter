import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException
from http import HTTPStatus


def get_currency_rate(from_currency, to_currency):
    URL = (f'https://www.xe.com/currencyconverter/convert/'
           f'?Amount=1&From={from_currency}&To={to_currency}')
    session = requests.Session()
    response = session.get(URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    p = soup.find('p', attrs={'class': 'result__BigRate-sc-1bsijpp-1 iGrAod'})
    if p is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проверьте правильность написания'
                   'введенной валюты и попробуйте позже'
        )
    p_text = ''.join(
        simbol if simbol.isdigit() else ' ' for simbol in p.text
        ).split()
    rate = f'{p_text[0]}.{p_text[1][:2]}'
    return rate
