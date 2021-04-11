class SushiPlatter():
    def __init__(self,salmon,tuna,shrimp,squid):
        self.salmon = salmon 
        self.tuna = tuna 
        self.shrimp = shrimp 
        self.squid = squid 

    @classmethod
    def lunch_special_A(cls):
        return cls(salmon =4,tuna =4,shrimp = 4,squid = 2)

    @classmethod
    def tuna_special(cls):
        return cls(salmon = 3,tuna = 2,shrimp = 5,squid =9)




boris = SushiPlatter(salmon = 2,tuna =5,shrimp = 5, squid = 3)
print(boris.salmon)



lunch_eaters = SushiPlatter.lunch_special_A()
print(lunch_eaters.salmon)
print(lunch_eaters.squid)

tuna_fan = SushiPlatter.tuna_special()
print(tuna_fan)
#print(boris)
print(tuna_fan.salmon)