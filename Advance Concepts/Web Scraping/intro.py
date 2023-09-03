import os
import requests
import bs4

os.system('cls')

print('\n------------example.com------------\n')
result = requests.get("https://example.com/")
# print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)
print(soup.select('title')) # Result is a string
print(type(soup.select('p')[0])) # Special Bs4 object
print(soup.select('title')[0].get_text())
print(soup.select('p'))
print(type(soup.select('p')[0]))
print(soup.select('p')[0].get_text())

print('\n------------wiki-Rakesh: Grab Content------------\n')
result = requests.get("https://en.wikipedia.org/wiki/Rakesh_Sharma")
soup = bs4.BeautifulSoup(result.text,"lxml")
# print(result.text)
for item in soup.select('.toctext'):
    print(item.get_text())

print('\n------------wiki-Rakesh: Grab Image------------\n')
# print(soup.select('img'))
for item in soup.select('img'):
    if "/Rakesh_sharma.jpg" in item['src']:
        print(item['src'])
        image_link_text = "https:"+item['src']
        print(image_link_text)

image_link= requests.get(image_link_text)
# print(image_link.content)
f = open('Rakesh_Sharma.jpg', 'wb') # wb = write binary
f.write(image_link.content)
f.close()