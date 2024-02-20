import re

def upandlow(text):
    sd = re.search('[A-Z][a-z]+', text)
    if sd:
        print(sd)
    else:
        print("Not match")

upandlow('Shhdhddhdhhd')