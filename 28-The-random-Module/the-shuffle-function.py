import random

characters = ["warrior", "Druids", "Hunter","Rogue","Mage"]

clone = characters[:]
clone = characters.copy()

random.shuffle(clone)

print(clone)
print(characters)
