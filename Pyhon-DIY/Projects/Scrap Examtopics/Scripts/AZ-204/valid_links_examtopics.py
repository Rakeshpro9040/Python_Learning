"""
Caution:
- Don't run this :( it can cause your MAC & IP address to be blocked by examptopics server. Fix is given Ref 2nd link.
- Probably test this in Azure VM after you are done with az-204 exam :), but
    do not run this in local, otherwise site will be in-accessible.
    But, after clearing cache & cookies in browser, the site become accessible.
- This query will hit the target url at a great speed, cause to ban your ip address by the host.
- For this sleep timer (min 15 sec) has been enabled, still running this script is not advisable.

Note:
- Prior running this script run "create_sorted_url_list.py"
Ref:
- https://www.geeksforgeeks.org/extract-title-from-a-webpage-using-python/
- https://stackoverflow.com/questions/57155387/workaround-for-blocked-get-requests-in-python
- https://www.whatsmyua.info/
- https://serpapi.com/blog/how-to-reduce-chance-of-being-blocked-while-web/
"""

from bs4 import BeautifulSoup
import requests
import time

with open("./output_links_tst_sorted.txt", "r") as a_file:
  for line in a_file:
    scrape_url = line.strip()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    result = requests.get(scrape_url, headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    # print(soup)
    print(soup.find_all('title'))

    # for title in soup.find_all('title'):
    #     if (title.get_text() == "ExamTopics - Exam Offline") \
    #             or (title.get_text() == "ExamTopics - Error"):
    #         print(title.get_text() + " ~~~ " + scrape_url)
    #     else:
    #         print(title.get_text() + " ~~~ " + scrape_url)
    # time.sleep(15)