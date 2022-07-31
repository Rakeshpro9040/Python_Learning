import os
import csv

os.system('cls')
print(os.getcwd())

# Step-1: Open the file
data = open(
    'D:\\C_Workspaces_Repositories\\GitHub_Repositories\\Python_Learning\\PDF & EXCEL\\example.csv', encoding='utf-8')

# Step-2: csv.reader
csv_data = csv.reader(data)

# Step-3: reformat it into a python object list of lists
data_lines = list(csv_data)

# Some Operations on csv
print(data_lines[1])  # Fetch Single row
print(data_lines[1][3])  # Fetch Single cell
all_emails = [line[3] for line in data_lines[1:10]]
print(all_emails)  # Fetch Single column
full_names = [line[1] + ' ' + line[2] for line in data_lines[1:10]]
print(full_names)

# Write to a csv
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])  # Single Row write
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6'],['7', '8', '9']])  # Multiple Row write

f_apppend = open('to_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(f_apppend)
csv_writer.writerow(['1','2','3'])