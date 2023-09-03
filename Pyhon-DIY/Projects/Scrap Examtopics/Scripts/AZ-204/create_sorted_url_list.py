"""
Note:
    Run this in PyCharm, due to relative path issue currently it does not work in VS code.
    This script will generate a csv file which can be sorted on topics & questions easily.
    But to automatically sort we may need pandas df.

Ref:
- https://www.geeksforgeeks.org/how-to-sort-data-by-column-in-a-csv-file-in-python/
- https://www.usepandas.com/csv/sort-csv-data-by-column
"""

import re
import pandas as pd
import os

print(os.getcwd())
mydict = dict()

# Empty the file, before append operation starts
with open("../../Outputs/output_links_sorted_temp.csv", "w") as fw:
    fw.write("Topic" + "," + "Question" + "," + "URL" + '\n')

with open("../Outputs/output_links.txt", "r") as a_file:
  for line in a_file:
    scrape_url = line.strip()
    # Build the dictionary with (index, url)
    matchObj = re.match(r'.*(/\d+\-(.*topic-(\d+)-question-(\d+).*)/$)', scrape_url, re.M | re.I)
    matchObj_gp0 = matchObj.group() # Form dictionary values, this will extract the whole url
    matchObj_gp1 = matchObj.group(1)
    matchObj_gp2 = matchObj.group(2)
    matchObj_gp3 = matchObj.group(3)
    matchObj_gp4 = matchObj.group(4)

    with open("../../Outputs/output_links_sorted_temp.csv", "a") as fa:
      fa.write(matchObj_gp3 + "," + matchObj_gp4 + "," + matchObj_gp0 + '\n')

# Sort the csv file using pandas
df = pd.read_csv("../../Outputs/output_links_sorted_temp.csv")
sorted_df = df.sort_values(by=["Topic", "Question"], ascending=True)
sorted_df.to_csv('../../Outputs/output_links_sorted.csv', index=False)