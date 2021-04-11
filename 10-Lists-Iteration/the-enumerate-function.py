errands = ["Go to gym","Grab lunch","Get promoted at work","Sleep"]

print(enumerate(errands))

for index, task in enumerate(errands):
    print(f"{task} is number {index} on my list of things to do today!")