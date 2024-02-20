import re

def space(text):
    x = re.subn("\s",":", text)
    y = re.subn("\s",",", text)
    print(x)
    print(y)



space("I'm Ualikhan and I love kitty")