import os
import requests
import bs4

os.system('cls')
url = 'https://www.codewithharry.com/'

# Step:1 - Get the HTML
r = requests.get(url)
htmlContent = r.text
# print(htmlContent)

# Step:2 - Parse the HTML # Here we use lxml
soup = bs4.BeautifulSoup(htmlContent, "lxml")
# print(soup.prettify)

# Step:3 - HTML Tree traversal
# Commonly used types of objects:
# 1. BeautifulSoup
soup = bs4.BeautifulSoup(htmlContent, "lxml")
print(type(soup))
# print(soup)

# 2. Tag
title = soup.title
print(type(title))
print(title)

# 3. NavigableString -- Special String
titleString = title.string
print(type(titleString))
print(titleString)

# 4. Comment

# 5. String
titleText = title.text
print(type(titleText))
print(titleText)

# 6. ResultSet
# Get all the paragraphs
paras = soup.find_all('p')
print(type(paras))
# print(paras)

# Get all the anchors
anchros = soup.find_all('a')
print(type(anchros))
# print(anchros)

# Get the first paragraph
para = soup.find('p')
print(type(para))
# print(para)

# Get the class from above paragraph -- Dictionary
# Get classes of any element in the HTML page
para_class = soup.find('p')['class']
print(type(para_class))
# print(para_class)

# Find all the elements with class lead
print(type(soup.find_all('p', class_="lead")))
# print(soup.find_all('p', class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())

# Get all teh text without any tags
# print(soup.get_text())

# Get all the links from teh page
anchros = soup.find_all('a')
# print(type(anchros[0]))
# print(anchros[2])
# print(anchros[2]['href'])
# print(anchros[2].get('href'))

all_links = {str(url + anchor['href']).strip() for anchor in anchros}
print(all_links)
