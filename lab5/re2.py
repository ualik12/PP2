import re

def text_match(text):
    sd = '^ab{2,3}$'
    if re.search(sd, text):
        return "Found a match"
    else:
        return "Not matched"
    
print(text_match("ab"))
print(text_match("abb"))
print(text_match("abbb"))
print(text_match("abbbb"))