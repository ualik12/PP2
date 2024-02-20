import re

def text_match(text):
    sd = '^a(b*)$'
    if re.search(sd, text):
        return "Found a match"
    else:
        return "Not mached"

print(text_match("abbbbb"))

#with open('row.txt','r') as file:
#    for line in file:
#        print(text_match(line.strip()))