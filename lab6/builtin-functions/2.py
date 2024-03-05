# variant - 1
string = str(input("Input any string: "))
giants = 0
dwarfs = 0
if len(string) != 0:
    for i in string:
        i = chr(i)
        if i >= 65 and i <= 90:
            giants += 1
        if i >= 97 and i <= 122:
            dwarfs += 1
print(f"Upper = {giants}, Lower = {dwarfs}")
# variant - 2
def count(string):
    hobit = sum(1 for c in string if c.isupper())
    ork = sum(1 for c in string if c.islower())
    return hobit, ork
army = str(input("Собери свою команду: "))

print(count(army))