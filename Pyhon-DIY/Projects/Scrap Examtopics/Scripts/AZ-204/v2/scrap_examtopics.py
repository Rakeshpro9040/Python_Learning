"""
Manually copy-paste the results from this query into "output_links.txt" file.
"""

from bs4 import BeautifulSoup
import requests

# if last page is 1012 then use range(1,1013)
for page_nbr in range(1, 4):
    print("Page-"+str(page_nbr))
    if page_nbr == 1:
        page_nbr = ''
    scrape_url = f"https://www.examtopics.com/discussions/microsoft/{page_nbr}"
    result = requests.get(scrape_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    for link in soup.find_all('a'):
        if "az-204" in str(link.get('href')):
            print("https://www.examtopics.com"+link.get('href'))