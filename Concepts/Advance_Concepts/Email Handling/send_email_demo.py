import os
import smtplib
import getpass

os.system('cls')
print(os.getcwd())

# Step-1 Create SMTP object
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
# 587: TLS
# 465: SSL

# Step-2 Greet the server
print(smtp_object.ehlo())

# Step-3 Initiate TLS
print(smtp_object.starttls())
# If Port 465 is used, then this step to be skipped

# Get the User Id and Password
# password = input('What is your password: ')
# This is not safe, as visible

# Use getpass
# password = getpass.getpass('What is your password: ')
# print(password)

# For gmail Users emable App password (two step auth is reqd)
email = input("Email: ")
password = getpass.getpass("Password: ")
print(smtp_object.login(email, password))
from_address = email
to_address = email
subject = input("Enter the subject line: ")
message = input("Enter the message body: ")
msg = "Subject: " + subject + '\n' + message
print(smtp_object.sendmail(from_address, to_address, msg))
print(smtp_object.quit())
