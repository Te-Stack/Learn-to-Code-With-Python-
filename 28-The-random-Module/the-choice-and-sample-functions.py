import random

print(random.choice(["Bob", "Moe", "Curly"]))

print(random.choice([1,2,3]))

lottery_number = [ random.randint(1,50)for value in range(50)]

print(random.sample(lottery_number,1))
print(random.sample(lottery_number,4))
