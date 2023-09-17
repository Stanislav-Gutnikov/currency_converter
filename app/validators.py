import re
from fastapi import HTTPException
from http import HTTPStatus


def is_currect_corrency(value):
    if (
        not re.search('[A-Z]', value) or
        len(value) != 3
    ):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проверьте правильность написания введенной валюты'
        )
    return value
