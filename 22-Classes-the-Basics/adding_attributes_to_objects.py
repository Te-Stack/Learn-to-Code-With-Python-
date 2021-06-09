class Guitar():
    def __init__(self):
        print(f"A new guitar is being created! This object is {self}")

acoustic = Guitar() 
electric = Guitar()

acoustic.wood = "Mohogany"
acoustic.wood = 7
acoustic.wood = 2001

electric.nickname = "Sound Viking 3000"

print(acoustic.wood)
print(electric.nickname)