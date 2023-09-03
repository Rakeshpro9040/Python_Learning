import os
import re

os.system('cls')
my_text = 'My primary phone number (555)-555-5555, Secondary phone number (444)-444-4444'
pattern1 = 'phone'

print('-----------Search------------')
match = re.search(pattern1,my_text) # This will return 1st match
print(match)
print(match.span())
print(match.start())
print(match.end())
print(match.group())

print('-----------Findall------------')
match = re.findall(pattern1,my_text) # This will return all match
print(match)
print(len(match))

print('-----------Finditer------------')
for match in re.finditer(pattern1,my_text):
    print(match)
    print(match.span())
    print(match.group())

print('-----------Reg Pattern:Identifiers------------')
for match in re.finditer(r'\(\d\d\d\)-\d\d\d-\d\d\d\d',my_text):
    print(match)
    print(match.span())
    print(match.group())


print('-----------Reg Pattern:Quantifiers------------')
for match in re.finditer(r'\(\d{3}\)-\d{3}-\d{4}',my_text):
    print(match.group())

print('-----------Reg Pattern:Compile with Group------------')
pattern1 = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{3})')
match = re.search(pattern1,my_text)
print(match.group(1))
print(match.group(2))
print(match.group(3))

print('-----------|(OR)------------')
my_text = 'men are male, women are female'
match = re.findall(r'men|women',my_text)
print(match)

text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
match = re.findall(r'cat(fish|nap|claw)',textthree)
print(match)

print('-----------.(period)------------')
my_text = 'The bat went splat'
match = re.findall(r'...at',my_text)
print(match)

print('-----------^$------------')
my_text = '1 The bat went splat _'
match = re.findall(r'^\d',my_text)
print(match)
match = re.findall(r'_$',my_text)
print(match)

print('-----------[^]+------------')
my_text = 'There are 3 numbers 34 inside 5 this sentence.'
match = re.findall(r'[^\d ]+',my_text)
print(match)
print(' '.join(match))

print('-----------Inclusion------------')
my_text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
match = re.findall(r'[\w]+-[\w]+',my_text)
print(match)