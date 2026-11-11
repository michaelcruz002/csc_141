
# 9-14 Lottery: Pick four winning numbers or letters.
from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

winning_ticket = []

while len(winning_ticket) < 4:
    number = choice(possibilities)

    if number not in winning_ticket:
        winning_ticket.append(number)

print("The winning ticket is:", winning_ticket)
print("Any ticket matching these four items wins a prize!")
