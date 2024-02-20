#Variant - 1 ___________
def generators(N):
    for i in range(1,N):
        print(pow(i, 2), end = " ")

N = int(input("Input any namber: "))
print("Result:")
generators(N)
#Variant - 2+++++++++++++
def squeres(end_point):
    count = 1
    while(count**2 <= end_point):
        yield count**2
        current+=1
print(*squeres(16))
#Varian - 3+++++++++++++
def number(start, stop):
    while(start<stop):
        yield start**2 # 1 4 
        start+=1
start = int(input("Input start: "))
stop = int(input("Input stop: "))
print(list(number()))