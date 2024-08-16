# WikiBot

### Бот для поиска в википедии.
[Бот](https://web.telegram.org/a/#7315661023)

### Технологии:
- Python 3.12
- BeautifulSoup
- telebot
- requests

### Об Авторе
[Вова Ушаков](https://github.com/Vova5454), 10 лет, студент курса python-разработки в Skysmart


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Vova5454/WikiBot.git
```

```
cd WikiBot
```

Cоздать и активировать виртуальное окружение:

```
# Для Windows:
python3 -m venv venv

# Для Mac и Linux:
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Создать нового бота в BotFather в Телеграме.

Получить API-токен и записать его в переменую token.