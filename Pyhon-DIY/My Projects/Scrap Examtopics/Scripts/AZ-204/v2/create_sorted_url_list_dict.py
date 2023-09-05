"""
Note:
    This does not sort the lines numerically, e.g. 10 comes after 1 instead of 2.
    For this we have to store the matchObj_gp3,matchObj_gp4,matchObj_gp0 into pandas df.
    Then do a sort operation on it.

    As this is still incomplete, use *csv.py which will generate a csv file.
"""

import re
import pandas as pd

mydict = dict()

with open("../Outputs/output_links.txt", "r") as a_file:
  for line in a_file:
    scrape_url = line.strip()
    # Build the dictionary with (index, url)
    matchObj = re.match(r'.*(/\d+\-(.*topic-(\d+)-question-(\d+).*)/$)', scrape_url, re.M | re.I)
    matchObj_gp0 = matchObj.group() # Form dictionary values, this will extract the whole url
    matchObj_gp1 = matchObj.group(1)
    matchObj_gp2 = matchObj.group(2) # Form dictionary keys, group(2) will fetch the most inner grou
    matchObj_gp3 = matchObj.group(3)
    matchObj_gp4 = matchObj.group(4)
    mydict[matchObj_gp2] = matchObj_gp0  # Form the dictionary

# Create a new dict after sorting mydict using keys
sorted_dict = {k:v for k,v in sorted(mydict.items())}

# Empty the file, before append operation starts
with open("../Outputs/output_links_sorted.txt", "w") as fw:
    pass

# Open teh file in append mode, then add values from the sorted dictionary
with open("../Outputs/output_links_sorted.txt", "a") as fa:
    for index, url in sorted_dict.items():
        fa.write(url + '\n')