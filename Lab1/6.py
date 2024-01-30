x = "cool man" # global variabls

def myfunc():
  print("Ualik is a " + x)

myfunc() #it tells the truth

print("Ualik_junior isn't a " + x)

"""
And We can make any variabls
to global variabls thanks to
"global" 
"""
x = "bad boy"

def myfunc():
  global x
  x = "fantastic man"

myfunc()

print("Ualik is a " + x)

"""
1)A variable name must start with a letter or the underscore character
2)A variable name cannot start with a number
3)A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4)Variable names are case-sensitive (age, Age and AGE are three different variables)
5)A variable name cannot be any of the Python keywords.
"""
