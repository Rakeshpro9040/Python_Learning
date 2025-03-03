import os
import requests
import bs4

os.system('cls')
base_url_test = "https://books.toscrape.com/catalogue/page-50.html"
result = requests.get(base_url_test)
# print(result.text)
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)
