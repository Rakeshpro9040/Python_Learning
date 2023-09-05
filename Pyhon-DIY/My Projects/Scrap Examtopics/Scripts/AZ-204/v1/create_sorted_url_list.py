import re

mydict = dict()

with open("../Outputs/output_links.txt", "r") as a_file:
  for line in a_file:
    scrape_url = line.strip()
    # Build the dictionary with (index, url)
    matchObj = re.match(r'.*(/\d+\-(.*)/$)', scrape_url, re.M | re.I)
    matchObj_gp0 = matchObj.group() # Form dictionary values, this will extract the whole url
    matchObj_gp2 = matchObj.group(2) # Form dictionary keys, group(2) will fetch the most inner group
    mydict[matchObj_gp2] = matchObj_gp0 # Form the dictionary

sorted_dict = {k:v for k,v in sorted(mydict.items())} # Create a new dict after sorting mydict using keys

# Empty the file, before append operation starts
with open("../Outputs/output_links_sorted.txt", "w") as fw:
    pass

# Open teh file in append mode, then add values from the sorted dictionary
with open("../Outputs/output_links_sorted.txt", "a") as fa:
    for index, url in sorted_dict.items():
        fa.write(url + '\n')