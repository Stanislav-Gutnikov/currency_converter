from fastapi import FastAPI

from .get_currency_rate import get_currency_rate
from .validators import is_currect_corrency


app = FastAPI()


@app.get('/')
def get_rate(from_currency: str, to_currency: str):
    is_currect_corrency(from_currency)
    is_currect_corrency(to_currency)
    rate = get_currency_rate(from_currency, to_currency)
    return rate
