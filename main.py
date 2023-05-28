import requests
import fake_useragent
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path


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
    servis_object = Service(binary_path)

    driver = webdriver.Chrome(service=servis_object)
    driver.maximize_window()
    driver.get("https://yandex.ru/search/?text=%D0%BC%D0%B5%D0%B4%D1%8C+%D0%BA%D1%83%D1%80%D1%81+%D1%86%D0%B5%D0%BD%D0%B0&lr=66")
    stock = driver.find_element(By.CLASS_NAME, 'StocksInfoBoard-Value').text
    stock_point = stock.replace(",", ".")
    stock_point = stock_point[:-2]
    return stock_point


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
