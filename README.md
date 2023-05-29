# copper_dollar
This script was developed by a student of yandex practicum, 59 cohort.
Implemented in terms of learning by doing.

Parses the dollar and copper quotes exchange output page with get-requests. Then sends everything to telegram bot at user's request.

## It is written using such technologies:

- [Python 3.10](https://docs.python.org/3.10/whatsnew/3.10.html)
- [Aiogram 2.25](https://docs.aiogram.dev/en/latest/)
- [Requests 2.31](https://requests.readthedocs.io/en/latest/)
- [Python-dotenv 1.0](https://github.com/theskumar/python-dotenv)

## Installation
**You need to clone the repository and go to it:**
```
git@github.com:PyMasterWeb-RU/copper_dollar.git
```
## Go to the project folder:##
```
cd copper_dollar
```
**Create and activate the virtual environment:**
```
python -m venv venv
source venv/Scripts/activate
```
**Install dependencies from requirements.txt file:**
```
pip install -r requirements.txt
```
**Create a .env file and put the bot's token in it:**
```
BOT_TOKEN=Here_is_your_bot's_token
```
**After that, run the bot:**
```
python bot.py
```
**Or if you want to run it without a console:**
```
pythonw bot.py
```

## Author: 
* [Kuznetsov Sergey](https://github.com/PyMasterWeb-RU) :+1:

**Communicate with the author:**
```
- Telegram: @PyMasterWeb
```