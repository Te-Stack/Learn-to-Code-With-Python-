check_prime = [26,39,51,53,57,79,85]

print(check_prime)


'''for el in check_prime:
    factor = []
    if el%2 ==0:
       print(f"{el} is not prime number")
    elif el%3 ==0:
        print(f"{el} is not prime number")
    elif el%5 ==0:
        print(f"{el} is not prime number")
    elif el%7 ==0:
        print(f"{el} is not prime number")
    else:
        print(f"{el} is  a prime number")'''

    
def prime(num):
    for el in num:
        if el%2 ==0:
            print(f"{el} is not prime number")
        elif el%3 ==0:
            print(f"{el} is not prime number")
        elif el%5 ==0:
            print(f"{el} is not prime number")
        elif el%7 ==0:
            print(f"{el} is not prime number")
        else:
            print(f"{el} is  a prime number")


prime(check_prime)


print(True)


Quincy = "i want to be a Security Software Engineer"
mind = "E hard o"
print(Quincy or mind)
print(Quincy == mind)