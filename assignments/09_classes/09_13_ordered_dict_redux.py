
# 9-13 Dice: Roll three different dice 10 times each.
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


die6 = Die()
print("Rolling a 6-sided die:")
for roll in range(10):
    die6.roll_die()

die10 = Die(10)
print("Rolling a 10-sided die:")
for roll in range(10):
    die10.roll_die()

die20 = Die(20)
print("Rolling a 20-sided die:")
for roll in range(10):
    die20.roll_die()
