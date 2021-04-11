class Emotion():
    def __init__(self,positivity,negativity):
        self.positivity = positivity
        self.negativity = negativity


    def __bool__(self):
        return self.positivity > self.negativity


my_emotional_state = Emotion(positivity = 80, negativity = 75)

if my_emotional_state:
    print("i don tire")