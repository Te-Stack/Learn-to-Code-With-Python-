flight_prices = {
    "Chicago":199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])
print(flight_prices["Denver"])

gym_membership_packages = {
    29:["Machines"],
    49:["Machines","Vitamin Supplement"],
    79:["Machines","Vitamin Supplement","Sauna"]
}

print(gym_membership_packages[49])
print(gym_membership_packages[79])

print(gym_membership_packages.get(29,["Basic Dumbells"]))
print(gym_membership_packages.get(100,["Basic Dumbells"]))
print(gym_membership_packages.get(100))

