class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(),cls()]
        print(f"New Number of counter object created:{cls.count}")
        return two_counters



print(Counter.count)
c1 = Counter()
print(Counter.count)

c2,c3 = Counter.create_two()

print(Counter.count)
print()
print(c1.count)
print(c2.count)
print(c3.count)


class Employee():
    numEmployee = 0

    def __init__(self, name, rate):
        self.owed = 0
        self.name = name
        self.rate=rate
        Employee.numEmployee += 1

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.owed += numHours * self.rate
        return(f"{numHours} hours worked")

    def pay(self):
        self.owed = 0
        return(f"payed {self.name}")


emp1 = Employee("Quincy",15.2)
print(emp1.hours(20))