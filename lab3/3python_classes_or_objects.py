#Как должен выглядить класс:
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

#Функцие инит в классах:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#Функцие стр в классах:
#Без него выведет сам объект (<__main__.Person object at 0x15039e602100>):
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
#С ним:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
#Объектный способ:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#Говорят о том, что self можно заменить на все что угодно
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
#Замена свойства:
p1.age = 40
#Удалить какое-то свойство объекта: 
del p1.age
#Удалить объект в принципе из класса:
del p1
#Пустой класс:
class Person:
  pass