import collections

Book = collections.namedtuple("Book",["title","author"])

animal_farm = Book("Animal Farm","George Orwell")
gatsby = Book( "The Great Gatsby","F.Scoot Fitzeralds")


class Library():
    def __init__(self,*books):
        self.books = books 
        self.librarian = []


    def __len__(self):
        return len(self.books)


L1 = Library(animal_farm)
L2 = Library(animal_farm,gatsby)


print(len(L1))
print(len(L2))