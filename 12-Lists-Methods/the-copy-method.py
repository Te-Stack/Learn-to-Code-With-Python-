Units = ["meter","kilogram","second","ampere","kelvin","candela","mole"]

More_units = Units.copy()

#print(Units)
#print(More_units)

Units.remove("kelvin")
print(Units)
print(More_units)

even_more_units = Units[:]
print(even_more_units)