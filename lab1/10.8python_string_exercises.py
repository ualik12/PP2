x = "Hello World"
print(len(x))
#======================================
txt = "Hello World"
x = txt[0]
print(x)
#======================================
x = txt[2:5]
print(x)
#======================================
txt = "Hello World "
x = txt.strip()
print(x)
#======================================
txt = " Hello World "
x = txt.strip()
print(x)
#======================================
txt = "Hello World"
x = txt.upper()
print(x)
#======================================
x = txt.lower()
print(x)
#======================================
x = txt.replace("H", "J")
print(x)
#======================================
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))