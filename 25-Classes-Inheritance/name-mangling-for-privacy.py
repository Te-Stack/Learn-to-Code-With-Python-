class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("This is coming from some_method!")

class SpecialNonsense(Nonsense):
    pass

n = Nonsense()
sn = SpecialNonsense()
#print(n.some_attribute)
#print(n.__some_method)


print(n._Nonsense__some_attribute)
print(sn._Nonsense__some_attribute)
n._Nonsense__some_method()
sn._Nonsense__some_method()