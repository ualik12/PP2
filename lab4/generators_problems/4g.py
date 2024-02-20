def squares(a, b):
    for i in range(a, b + 1):
        yield i**2
a = int(input("Begin: "))
b = int(input("End: "))
tuple1 = tuple(squares(a, b))
new_tuple = map(str, tuple1)
result = ", ".join(new_tuple)
print(result)
# or
print(*squares(4,8))
