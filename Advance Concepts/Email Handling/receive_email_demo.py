import os
import imaplib
import getpass
import email

os.system('cls')
M = imaplib.IMAP4_SSL('imap.gmail.com') # Initialize

email_id = input("Email: ")
password = getpass.getpass("Password: ")

print(M.login(email_id, password))
# print(M.list()) # Anything to be checked in email

# Step: Select Inbox
print(M.select('inbox')) # To scan inbox

# Step: Search in Inbox
typ, data = M.search(None, 'SUBJECT "NEW TEST PYTHON"') # Returns Tuple
# Can be serached using Date, From, ..
print(typ)
email_id = data # Data of all email id
print(email_id)
email_id = data[0]
print(email_id) # Returns Unique Id

# Step: Fetch Email Data
result, email_data = M.fetch(email_id, '(RFC822)') # Fetch a particular Email Id using a protocol
print(result)
print(email_data)
raw_email = email_data[0][1] 
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)
print(type(email_message))
print(email_message)
for part in email_message.walk():
    if part.get_content_type() == 'text/plain': # If there is a link use text/html
        body = part.get_payload(decode=True)
        print(body)