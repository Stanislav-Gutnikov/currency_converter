# currency_converter
Конвертер валют

### Описание ###
Введите две валюты чтобы узнать курс первой валюты ко второй.

### Установка ###

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Stanislav-Gutnikov/currency_converter.git
```

Cоздать и активировать виртуальное окружение с помощью ctrl+shift+p (VSC)

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить проект:

```
uvicorn app.main:app
```