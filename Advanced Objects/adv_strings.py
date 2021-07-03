import os

os.system('cls')

s = 'hello World'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.count('o'))
print(s.find('o'))
print(s.center(20,'z')) # Center bet z with tot len 20
print('hello\thi')
print('hello\thi'.expandtabs())
s = 'hello'
print(s.isalnum()) # Is all alphanumeric
print(s.isalpha()) # Is all alphabate
print(s.islower()) # Is all lower
print(s.isspace())
print(s.istitle()) # Is a title like Hello
print(s.endswith('o'))
print(s[-1] == 'o')
print(s.split('e')) # split at e
print(s.partition('e')) 
# It will spilt at 1st occ and also include separator