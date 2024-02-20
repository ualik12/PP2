import re

def text_match(text):
    sd = re.search('[a-z]_', text)
    if sd:
        print(sd)
    else:
        print("no match")

text_match('a_d_dfsd,s')
