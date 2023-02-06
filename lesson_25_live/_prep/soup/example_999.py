from bs4 import BeautifulSoup
import requests

prive_value_class = "adPage__content__price-feature__prices__price__value"
price_currency_class = "adPage__content__price-feature__prices__price__currency"

url = input('Enter 999 url to find price')
data = requests.get(url)
soup = BeautifulSoup(data.content)

price = float(soup.find('span', {"class": prive_value_class}).text.strip().replace(' ', ''))
currrency = soup.find('span', {"class": price_currency_class}).text.strip()
print(f'Price is {price} {currrency}')
