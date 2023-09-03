import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    if set(alphabet) == set(str1.replace(' ','').lower()):
        print('Yes')
    else:
        print('No')
    return set(alphabet).issuperset(set(str1.replace(' ','').lower()))

str1 = "The quick brown fox jumps over the lazy dog"
print(ispangram(str1))
print(set(str1.replace(' ','').lower()))
print(set(string.ascii_lowercase))
