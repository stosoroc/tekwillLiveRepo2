import requests
from bs4 import BeautifulSoup

response = requests.get('https://ro.wikipedia.org/wiki/Republica_Moldova')

soup = BeautifulSoup(response.content)

article_content = soup.find("div", {"id": "mw-content-text"})
inner_article_items = article_content.find("div", {"class": "mw-parser-output"}).find_all("p")
all_article_text = [item.text for item in inner_article_items]
print(all_article_text)
# A lot of text
all_images = soup.find_all('img')
all_images_sources = [img.get('src') for img in all_images]
print(all_images_sources)
# A lot of images
