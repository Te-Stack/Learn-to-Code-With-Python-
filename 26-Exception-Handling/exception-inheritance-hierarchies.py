class Mistake(Exception):
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass


try:
    raise StupidMistake("Extra Stupid Mistake")
except StupidMistake as e:
    print(f"Caught the error:{e}")

try:
    raise StupidMistake("Extra Stupid Mistake")
except Mistake as e:
    print(f"Caught the error:{e}")


try:
    raise SillyMistake("Super Silly Mistake")
except Mistake as e:
    print(f"Caught the error:{e}")

