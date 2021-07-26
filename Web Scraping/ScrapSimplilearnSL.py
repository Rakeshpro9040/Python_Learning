import os
import requests
import bs4

os.system('cls')

print('\n------------Start Scraping------------\n')
result = requests.get('https://quotes.toscrape.com/page/1/')
soup = bs4.BeautifulSoup(result.text, "lxml")