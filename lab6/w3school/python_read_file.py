f = open("demofile.txt", "r")
print(f.read())
# ------------------------------------------------------------------
# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())
"""
Welcome to this text file!
This file is located in a folder named "myfiles", on the D drive.
Good Luck!
"""
# ------------------------------------------------------------------
f = open("demofile.txt", "r")
print(f.read(5))
# ------------------------------------------------------------------
f = open("demofile.txt", "r")
print(f.readline())
# ------------------------------------------------------------------
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
# ------------------------------------------------------------------
f = open("demofile.txt", "r")
for x in f:
    print(x)
# ------------------------------------------------------------------
f = open("demofile.txt", "r")
print(f.readline())
f.close()