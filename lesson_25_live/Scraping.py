import requests
from bs4 import BeautifulSoup
import pandas as pd


# headers = {
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
# }

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}


print()
# Realizeaza cererea HTTP si returneaza continutul site-ului
film = input("Nume Film care a fost in cinema, fara seriale si filme anuntate: ")
url = "https://www.imdb.com/find/?q=" + film + "&ref_=nv_sr_sm"
print("Caut film in baza IMDb...")
page = requests.get(url, headers=headers)

# Parsing HTML cu BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Gasiti toate elementele cu eticheta "table" si selectati prima
table = soup.find("div", {'class':"ipc-metadata-list-summary-item__tc"})
link = table.find("a", {'class':"ipc-metadata-list-summary-item__t"})
ln = link.get("href")
print("Am gasit film pe adresa: ", ln)
print("Caut informatii despre film...")
url2 = "https://www.imdb.com" + ln
page = requests.get(url2, headers=headers, proxies=proxies)

# Parsing HTML cu BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Gasiti toate elementele cu eticheta "table" si selectati prima
table = soup.find("div", {'class':"sc-b5e8e7ce-0 dZsEkQ"})
table = table.find("div", {'class':"ipc-btn__text"})

# table = table.find("div", {'class':"sc-f6306ea-3 eGCTqT"})
# table = table.find("div", {'class':"sc-7ab21ed2-0 kkdwNM"})
# table = table.find("div", {'class':"sc-7ab21ed2-2 gWdbeG"})
# print(table)
imdb = table.find("span", {'class':"sc-7ab21ed2-1 eUYAaq"}).text
#print (imdb)

table = soup.find("section", {'data-testid':"BoxOffice"})
table = table.find("li", {'data-testid':"title-boxoffice-cumulativeworldwidegross"})
cost = table.find("label", {"class":"ipc-metadata-list-item__list-content-item"}).text
#print(cost)
print(f"Film '{film.upper()}' are nota {imdb} pe IMDb, acumulat {cost} in toata lumea")
print()

# # Parsing tabelul cu Pandas
# df = pd.read_html(str(table))[0]

# # Salvarea datelor in formatul Excel
# df.to_excel("data.xlsx", index=False)
