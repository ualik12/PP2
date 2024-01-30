x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x))
print(type(y))
print(type(z))


family = ["Ualik_1","Ualik_2","Ualik_3"]
x, y, z = family
print(x)
print(y)
print(z)

x = y = "Orange"
z = "Blue"

print(x)
print(y)
print(z)

if x == "Orange" and y == "Orange":
    z = "Orange"
print(x)
print(y)
print(z)