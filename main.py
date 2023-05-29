import requests
import fake_useragent
from bs4 import BeautifulSoup


def dollars():
    session = requests.Session()

    link_stock = "https://cbr.ru/search/?text=доллар"

    user = fake_useragent.UserAgent().random

    header = {
        'User-Agent': user
    }

    response = session.post(link_stock, headers=header).text

    soup = BeautifulSoup(response, 'html.parser')

    # currency_title = soup.find("div", class_="currency_title").text

    # currency_symbol = soup.find("div", class_ = "currency_symbol").text

    currency_price = soup.find("div", class_ = "currency_price").text
    currency_price = currency_price[2:]
    currency_point = currency_price.replace(",", ".")
    
    return currency_point

def medium():
    session = requests.Session()
    link = 'https://goramet.ru/ceni-na-cvetnie-metalli/'

    headers = {
        'User-Agent': fake_useragent.UserAgent().random
    }

    response = session.get(link, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    currency_price = (soup.select_one("table tr:nth-of-type(3)")).text

    currency_copper = currency_price[4:-9]
    return currency_copper


def price_change():
    currensy = dollars()
    copper = medium()
    price = float(copper) * float(currensy)
    price = int(price)
    price_change = int(price / 1000) - 70
    return price_change


def copper_rub():
    currensy = dollars()
    copper = medium()
    price = float(copper) * float(currensy)
    price = int(price)
    return price
    

if __name__ == "__main__":
    currensy = dollars()
    copper = medium()
    price = float(copper) * float(currensy)
    price = int(price)
    price_change = int(price / 1000) - 70
    print(f"""Цена меди: {copper}
Курс доллара: {currensy}
Цена меди в рублях: {price}
Предположительная цена сдачи в рублях: {price_change}
          """)
