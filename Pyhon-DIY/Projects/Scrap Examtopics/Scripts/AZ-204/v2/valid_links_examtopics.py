"""
Caution:
- This query will hit the target url at a great speed, cause to ban your ip address by the host.
- For this sleep timer (min 15 sec) has been enabled, still running this script is not advisible.

Note:
- Prior running this script run "create_sorted_url_list.py"
Ref:
- https://www.geeksforgeeks.org/extract-title-from-a-webpage-using-python/
"""

from bs4 import BeautifulSoup
import requests
import time

with open("../Outputs/output_links_sorted.txt", "r") as a_file:
  for line in a_file:
    scrape_url = line.strip()
    result = requests.get(scrape_url)
    soup = BeautifulSoup(result.text, 'html.parser')

    for title in soup.find_all('title'):
        if (title.get_text() == "ExamTopics - Exam Offline") \
                or (title.get_text() == "ExamTopics - Error"):
            print(title.get_text() + " ~~~ " + scrape_url)
        else:
            print(scrape_url)
    time.sleep(15)