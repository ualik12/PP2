import re

text = str(input("Введите свой номер: "))
sd1 = re.search(r"^(\+7)?(8)?-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$", text)
if sd1 :
    print("Да")
else:
    print("No")