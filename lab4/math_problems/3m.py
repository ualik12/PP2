import math
def S(a, n):
    s = int((n*pow(a, 2))/(4*math.tan((math.pi/n))))
    print(f"The area of the polygon is: {s}")
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))