import collections

Book = collections.namedtuple("Book",["title","author"])

animal_farm = Book("Animal Farm","George Orwell")
gatsby = Book( "The Great Gatsby","F.Scoot Fitzeralds")

print(animal_farm[0])
print(gatsby[1])

print(animal_farm.title)
print(gatsby.author)