class generators:
    def __init__(self, n):
        self.start = 0
        self.end_point = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end_point+1:
            raise StopIteration()
        self.start+=12
        return self.start - 12
        
n = int(input())
for i in generators(n):
    print(i)
#Variant - 2
def need(stop):
    start = 0
    while start < stop+1:
        if start / 12 == 0:
            yield start

s = int(input("Input finall point: "))
t = tuple(need(s))
nt = map(str, t)
result = ", ".join(nt)
print(result)