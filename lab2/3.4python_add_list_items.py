thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #push_back в с++
print(thislist)
#==============================================
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#==============================================
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #Использовать, чтобы прибваить два списка
print(thislist)
#==============================================
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) #И не только со списками
print(thislist)