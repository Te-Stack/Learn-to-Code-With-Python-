mountains = ["Mount Everest","K2"]
print(mountains)

mountains.extend(["Kangchenjuga","Lhotse","Makalu"])
print(mountains)

extra_mountains = ["Cho Oyu","Dhaulagri"]
mountains.extend(extra_mountains)
print(mountains)

print()

mountains.extend([])
print(mountains)

print()

steaks = ["Tenderloin","New York Strip"]
more_steaks = ["T-Bone","Ribeye"]

my_meal = steaks + more_steaks
print(my_meal)
print(steaks)
print(more_steaks)