

class CustomList():
    def __init__(self,element = 1):
        self.my_custom_list = [0] * element 

    def __str__(self):
        return "Afa na:"+ str(self.my_custom_list)


    def __setitem__(self,index,value):
        self.my_custom_list[index] = value

    def __getitem__(self,index):
        return (f"Hey You are accessing {index} element whose value is: {self.my_custom_list[index]}")



print(CustomList())

obj = CustomList(12)
obj[0] = 1

print(obj[0])
print(obj)

