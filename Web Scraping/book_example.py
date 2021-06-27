import os
import requests
import bs4

os.system('cls')

print('\n------------Dynamic Page------------\n')
for page_nbr in range(1, 51):
    base_url = f"https://books.toscrape.com/catalogue/page-{page_nbr}.html"
    # print(base_url)

base_url_test = "https://books.toscrape.com/catalogue/page-50.html"
result = requests.get(base_url_test)
# print(result.text)
soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)
# print(soup.select(".product_pod"))
# print(len(soup.select(".product_pod"))) # 20 Books

print('\n------------Loop Through the Page------------\n')
books = soup.select(".product_pod")
# print(type(books))
# print(books[0])
book_first = books[0]
# print(book_first.select(".star-rating.Two")) # f=For Space use . in css class
if book_first.select(".star-rating.Two") != []:
    pass
    # print(book_first.select('a')[1]['title'])

print('\n------------Main Logic------------\n')
for page_nbr in range(1, 51):
    scrape_url = f"https://books.toscrape.com/catalogue/page-{page_nbr}.html"
    result = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select(".star-rating.Five")) != 0:
            book_title = book.select('a')[1]['title']
            print(str(page_nbr) + '--> ' + book_title)
