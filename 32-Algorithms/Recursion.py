# def countdown(i):
#  print i
#  if i <= 0: #Base case
#  return
#  else: #Recursive case
#  countdown(i-1)

def countdown(i):
    print(i)
    if i<= 0: #base case 
        return
    else: #Recursive case
        countdown(i-1)


countdown(3)

print()
#Factorial 
def fact(x):
 if x == 1:
    return 1
 else:
    return x * fact(x-1)

print(fact(5))