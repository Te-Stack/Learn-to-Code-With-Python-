print(type({"a": 1}))

print(isinstance(1,int))
print(isinstance([],list))

print(isinstance(1,object))
print(isinstance(3.4,object))
print(isinstance(str,object))
print()

print(isinstance([],(list,dict,int)))
print()

class Person():
    pass

class Superhero(Person):
    pass


arnold = Person()
quincy = Superhero()

print(isinstance(quincy,Superhero))
print(isinstance(quincy,Person))
print(isinstance(arnold,Superhero))

print(issubclass(Superhero,Person))
print(issubclass(Person,Superhero))