
# 7-10 Dream Vacation: Ask people where they would like to visit.

vacations = {}

while True:
    name = input("What is your name? ")
    place = input("Where would you like to go on vacation? ")
    vacations[name] = place

    again = input("Does someone else want to answer? (yes/no): ")
    if again == "no":
        break

print("Dream vacation results:")
for name, place in vacations.items():
    print(f"{name} wants to visit {place}.")
