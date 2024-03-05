import os

path = 'delete.txt'

if os.path.exists(path):
    os.remove(path)
else:
    print("file doesn't exists")
   