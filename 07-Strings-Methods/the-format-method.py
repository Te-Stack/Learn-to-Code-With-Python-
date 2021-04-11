#name,adjective and noun
#mad_lips = "{} laughed at the {} {}."

#print(mad_lips.format("Quincy","silly",'tomato'))

mad_lips = "{name} laughed at the {adjective} {noun}."

name = input("Enter a name: ")
adjective = input("Enter an Adjective: ")
noun = input("Enter a noun: ")

print(mad_lips.format(name =name,adjective = adjective,noun = noun))