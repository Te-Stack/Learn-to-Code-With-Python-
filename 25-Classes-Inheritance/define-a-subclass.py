class Store():
    def __init__(self):
        self.owner ="Quincy"

    def exclaim(self):
        return "lots of stuff to buy,come inside or!"


class CoffeeShop(Store):
    pass

starbuck = CoffeeShop()

print(starbuck.owner)
print(starbuck.exclaim())

