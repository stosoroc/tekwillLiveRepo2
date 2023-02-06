import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_price_for_url(url):
    price_class = 'adPage__content__price-feature__prices__price__value'
    currency_class = 'adPage__content__price-feature__prices__price__currency'
    data = requests.get(url)
    soup = BeautifulSoup(data.content, features="html.parser")
    item_name = soup.find('h1', attrs={'itemprop': 'name'}).text
    try:
        price = int(
            soup.find(attrs={'class': price_class}).text.strip().replace(' ',
                                                                         ''))
    except ValueError:
        return
    currency = soup.find(attrs={'class': currency_class}).text
    images = soup.find_all('a', attrs={'class': 'mfp-image', 'data-fancybox': 'gallery'})
    images_urls = [image.get('data-src') for image in images]
    return dict(
        item_name=item_name,
        price=price,
        currency=currency,
        images_urls=images_urls,
    )


def search_999(query, search_url):
    scrap = True
    page_indx = 1
    links = []
    while scrap:
        print('Scrapping page', page_indx)
        response = requests.get(
            search_url,
            params={
                'query': query,
                'page': page_indx

            }
        )
        soup = BeautifulSoup(response.content, features="html.parser")
        all_ads = soup.find_all('li', attrs={'class': 'ads-list-photo-item'})
        links_found = []
        for ad in all_ads:
            try:
                link = ad.find('a', attrs={'class': 'ads-list-photo-item-animated-link'})
                if 'booster' in str(link):
                    continue
                link_href = link.get('href')
                links_found.append(f'https://999.md{link_href}')
            except Exception as ex:
                print(ex)
        if not links_found:
            break
        page_indx += 1
        links.extend(links_found)

    return links


#
# url = input('Enter 999 url to find price')
# print(get_price_for_url(url))

def search_tablets_on_999():
    tablet_name = input()
    links = search_999(tablet_name, 'https://999.md/ru/list/computers-and-office-equipment/tablet')
    data_list = []
    for idx, link in enumerate(links):
        print('Parsing link nr', idx + 1, f'out of {len(links)}')
        data = get_price_for_url(link)
        if data:
            data_list.append(data)
    pd.DataFrame(data_list).to_excel('scrapped_data.xlsx')


search_tablets_on_999()
