from random import randint

class Dice:
    def __init__ (self, value):
        self.value = value

    def roll_6_die(self):
        return randint(1,6)

test = roll_6_die(6)