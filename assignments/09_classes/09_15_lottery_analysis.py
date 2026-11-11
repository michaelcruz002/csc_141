
# 9-15 Lottery Analysis: Count how many tries it takes to win.
from random import sample

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

my_ticket = [1, 5, "a", "d"]
attempts = 0

while True:
    winning_ticket = sample(possibilities, 4)
    attempts += 1

    if set(winning_ticket) == set(my_ticket):
        break

print("My ticket:", my_ticket)
print("Winning ticket:", winning_ticket)
print("It took", attempts, "tries to win!")
