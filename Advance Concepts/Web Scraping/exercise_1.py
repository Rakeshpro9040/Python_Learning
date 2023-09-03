import os
import requests
import bs4

os.system('cls')

print('\n------------Start Scraping------------\n')
result = requests.get('https://quotes.toscrape.com/page/1/')
soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)
# soup = bs4.BeautifulSoup(result.text, 'html.parser')
# print(soup)
# tags = {tag.name for tag in soup.find_all()}
# print(tags)
# tags = {tag for tag in soup.find_all('div')}
# tag_pop = tags.pop()
# print(tag_pop)
# print(tag_pop.has_attr("class"))
# print(tag_pop['class'])

print('\n------------TASK: Get the names of all the authors on the first page.------------\n')
authors = soup.select(".author")
# print(type(authors))
# print(authors)
# print(type(authors[0]))
# print(type(authors[0].text))
# print(authors[0].text.strip())


# for author in authors:
#     print(author.text.strip())

# Set Comprehension
author_list = list({author.text.strip() for author in authors})
print(author_list)

print('\n------------TASK: Create a list of all the quotes on the first page.------------\n')
quotes = soup.select(".quote")
# print(type(quotes[0]))
# quote_1 = quotes[0].span.text.strip()
# quote_translation_from = ""
# quote_translation_to = ""
# quote_translation_remove = "“”"
# quote_translation = quote_1.maketrans(
#     quote_translation_from, quote_translation_to, quote_translation_remove)
# quote_translation = quote_1.maketrans(
#     "", "", quote_translation_remove)
# print(quote_translation)
# print(quote_1.replace('“', '').replace('”', ''))
# print(quote_1.translate(quote_translation))
# quote_list = list({quotes.text.strip() for quote in quotes})
# print(quote_list)

quote_list = []
for quote in quotes:
    quote_text = quote.span.text.strip()
    quote_translation_remove = "“”"
    quote_translation = quote_text.maketrans(
        "", "", quote_translation_remove)
    quote_list.append(quote_text.translate(quote_translation))
print(quote_list)


# print('\n------------TASK: String Translation.------------\n')
# first string
# firstString = "abc"
# secondString = "ghi"
# thirdString = "ab"

# string = "abcdefa"
# print("Original string:", string)

# translation = string.maketrans(firstString, secondString, thirdString)
# translation = string.maketrans(firstString, secondString) # This creates a dictionary with ASCII vlaues

# translate string
# print("Translated string:", string.translate(translation))

print("""\n------------
TASK: Inspect the site and use Beautiful Soup to extract the top ten tags
from the requests text shown on the top right from the home page(e.g Love, Inspirational, Life, etc...).
HINT: Keep in mind there are also tags underneath each quote,
try to find a class only present in the top right tags, perhaps check the span.
------------\n""")
tag_div = soup.select(".tag-item")
# print(type(tag_div))
# print(type(tag_div[0]))
# print(tag_div[0].attrs)
# print(tag_div[0].name)
# print(tag_div[0].text)
# print(tag_div[1].text)
tag_list = [tags.text.strip() for tags in tag_div]
print(tag_list)

print("""\n------------TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. 
Keep in mind there are many ways to achieve this, also note that you will need to somehow figure out how to check that your loop 
is on the last page with quotes. For debugging purposes, I will let you know that there are only 10 pages, 
so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that it wouldn't 
matter to know the amount of pages beforehand, perhaps use try/except for this, its up to you!------------\n""")
