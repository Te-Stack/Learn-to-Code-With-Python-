stats = {
    "name":"BBQ Chicken",
    "price":19.99,
    "size":"extra large",
    "ingredient":["Chicken","Onions","BBQ Sauce"]
}

class Pizza():
    def __init__(self,stats):
        for key,value in stats.items():
            setattr(self,key,value)


bbq = Pizza(stats)

print(bbq.size)
print(bbq.name)

for attr in ["price","ingredient","quincy","anointed"]:
    print(getattr(bbq,attr,"Unknown"))