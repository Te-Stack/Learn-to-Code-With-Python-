numbers = [3,4,5,6,7]
squares = []

for number in numbers:
    squares.append(number **2)
print(squares)    

squares = [number **2 for number in numbers]
print(squares)

rivers = ["Amazon","Nile","Yandtze"]
print([len(river) for river in rivers])


expressions = ["lol","rofl","Lmao"]
print([expression.upper() for expression in expressions])

decimals = [4.95, 3.28, 1.08]
print([int(decimal) for decimal in decimals])


#using list comprehensions for Cartesian Products

students = ["quincy","iyanu","samuel"]
levels = [1,2,3,5]

student_check = [(student,level)for student in students for level in levels]
print(student_check)
