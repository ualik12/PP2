def gen(N):
    i = 0
    while N > i:
        yield N
        N -= 1
for i in gen(int(input())):
    print(i)