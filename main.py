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

    currency_price = soup.find("div", class_ = "currency_price").text
    currency_price = currency_price[2:]
    currency_point = currency_price.replace(",", ".")
    
    return currency_point

def medium():
    
    url = 'https://mfd.ru/marketdata/ticker/?id=15277#id=15277'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    price_copper = soup.find('div', class_ = 'm-companytable-last').text
    price_copper_final = price_copper.replace(" ", "")
    return float(price_copper_final)


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
