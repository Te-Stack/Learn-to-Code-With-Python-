import re 
pattern = re.compile("flower")

match = pattern.match("flower in the field")

print(match)


print()

sentence = "There are a lot of flowers in the flowery flower field."
print(pattern.findall(sentence))
print(pattern.findall("Nonsense"))

for el in pattern.finditer(sentence):
    print(el)

    
print()

print(re.search("flower","Picking flowers in the flower field"))
print(re.match("flower","flower  "))

print()

print("\tTake a look.There is a tab and line break\n right here.")
print(r"Take a look.There is a tab and line break right here")

print()

more = re.compile(r"\d")

words = "I went to the store and brought 5 apples,4 oranges, and 15 plums."
print(more.findall(words))

print()

more = re.compile(r"\D")
print(more.findall(words))

print()

more = re.compile(r"\s")
print(more.findall(words))

print()

more = re.compile(r"\S")
print(more.findall(words))

print()

more = re.compile(r"\w")
print(more.findall(words))