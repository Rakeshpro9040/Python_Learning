import os
import requests
from bs4 import BeautifulSoup

os.system('cls')

print('\n------------Start Scraping------------\n')
# result = requests.get('https://accounts.simplilearn.com/user/login')
# soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)

login_url = 'https://accounts.simplilearn.com/user/login'
data = {
    'username': 'rakeshroshanpanigrahipro@gmail.com',
    'password': 'One@panda10'
}

with requests.Session() as s:
    response = requests.post(login_url , data)
    print(response.text)
    index_page= s.get('https://lms.simplilearn.com/courses/2772/Data-Science-with-Python/syllabus')
    soup = BeautifulSoup(index_page.text, 'html.parser')
    print(soup.title)
