#Variant - 1
def nnn(N):
    start = 0
    while start < N:
        if start % 2 == 0:
            yield start
        start+=1

nnnnn = tuple(nnn(20))
newtuple=map(str, nnnnn)
res=", ".join(newtuple)
print(res)
#Variant - 2
class evennumber:
    def __init__(self, n):
        self.n = n
        self.even = 0
        self.end_point = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.even > self.end_point:
            raise StopIteration()
        x = self.even
        self.even +=2
        return x
N = int(input("Input num: "))
for i in evennumber(N):
    print(i)
