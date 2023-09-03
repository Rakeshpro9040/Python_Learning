import re
import pandas as pd

mydict = dict()

with open("../../../Outputs/Test/output_links_tst.txt", "r") as a_file:
  for line in a_file:
    scrape_url = line.strip()
    # Build the dictionary with (index, url)
    matchObj = re.match(r'.*(/\d+\-(.*topic-(\d+)-question-(\d+).*)/$)', scrape_url, re.M | re.I)
    matchObj_gp0 = matchObj.group() # Form dictionary values, this will extract the whole url
    matchObj_gp1 = matchObj.group(1)
    matchObj_gp2 = matchObj.group(2)
    matchObj_gp3 = matchObj.group(3)
    matchObj_gp4 = matchObj.group(4)

    print(matchObj_gp3 + "," + matchObj_gp4 + "," + matchObj_gp0)