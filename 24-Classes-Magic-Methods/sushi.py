"""
A module related to the joy of sushi.
No fishy code found here 
"""
def fish():
    """
    determine if fish is a good meat choice.
    Always returns True,because it always is
    """
    return True


class Salmon():
    """
    Blueprint for a salmon object
    """
    def __init__(self):
        self.tastiness = 10

    def bake(self):
        """
        Bake the fish
        """
        self.tastiness += 1