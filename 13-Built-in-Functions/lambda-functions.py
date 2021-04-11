metals = ["gold", "silver"," platinium","palladium"]

print(list(filter(lambda metal: len(metal) > 5,metals)))
print(list(filter(lambda word: "p" in word,metals)))

print(list(map(lambda word: word.count("l"),metals)))
print(list(map(lambda val: val.replace("s","$"), metals)))