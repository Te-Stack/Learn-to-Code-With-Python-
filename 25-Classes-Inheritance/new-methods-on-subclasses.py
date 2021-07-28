class Employee():
    def do_work(self):
        print("I'm working and I am tired")

class Manager(Employee):
    def waste_time(self):
        print("Wow,this youtube video looks fun!")

class Director(Manager):
    def fire(self):
        print("you're fired!")

    
e = Employee()
m = Manager()
d = Director()

e.do_work()

m.do_work()
m.waste_time()

d.waste_time()
d.do_work()
d.fire()