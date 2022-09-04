ingredient = ("Chicken","Beef",375,30)

print(ingredient)

meats,spice,temperature,cooking_time = ingredient

print(meats)
print(cooking_time)

#grab excess items with *

a,b,*rest=range(7)
print(a)
print(b)
print(*rest)