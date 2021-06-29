import os
import csv

os.system('cls')
print(os.getcwd())

# Step-1: Open the file
data = open(
    'C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\PDF & EXCEL\\example.csv', encoding='utf-8')

# Step-2: csv.reader
csv_data = csv.reader(data)

# Step-3: reformat it into a python object list of lists
data_lines = list(csv_data)
print(data_lines[1])  # Fetch Single row
print(data_lines[1][3])  # Fetch Single cell
all_emails = [line[3] for line in data_lines[1:10]]
print(all_emails)  # Fetch Single column
