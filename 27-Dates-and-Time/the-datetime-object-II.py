from datetime import datetime 

today = datetime.today()

print(today.strftime("%m"))
print(today.strftime("%m %d"))
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%d-%m-%Y"))

print(today.strftime("%Y-%m-%d"))
print(today.strftime("%y-%m-%d"))


print(today.strftime("%a"))
print(today.strftime("%B"))

print(today.strftime("%j"))
print(today.strftime("%W"))




