import re

def aandb(text):
    sd = re.search('a.*?b$', text)
    if sd:
        return "Founde a match"
    else:
        return "Not matched"
    
print(aandb('aashhdgxpgdgsv,bhshs'))
print(aandb('asb'))
print(aandb('aashahd'))