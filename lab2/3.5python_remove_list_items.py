thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #Чтобы удалить
print(thislist)
#===============================================================================================
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") #Удаляет только первый banana
print(thislist)
#===============================================================================================
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#===============================================================================================
thislist = ["apple", "banana", "cherry"]
thislist.pop() #Удаляет конец List
print(thislist)
#===============================================================================================
thislist = ["apple", "banana", "cherry"]
del thislist[0] #Удалит по индексу
print(thislist)
#===============================================================================================
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
#===============================================================================================
thislist = ["apple", "banana", "cherry"]
thislist.clear() #Чистит
print(thislist)