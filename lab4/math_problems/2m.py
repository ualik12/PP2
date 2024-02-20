def S(a, b, c):
    d = a + b
    S = (d/2)*c
    print(f"Expected Output: {S:.1f}")

c = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
S(a, b, c)