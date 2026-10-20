
# 7-6 Three Exits: Show three simple ways to stop a loop.

# Way 1: Check a condition in the while line.
topping = ""
while topping != "quit":
    topping = input("Way 1 - Enter a topping (or quit): ")
    if topping != "quit":
        print(f"Adding {topping}.")

# Way 2: Use a True or False variable.
active = True
while active:
    topping = input("Way 2 - Enter a topping (or quit): ")
    if topping == "quit":
        active = False
    else:
        print(f"Adding {topping}.")

# Way 3: Use break to stop the loop.
while True:
    topping = input("Way 3 - Enter a topping (or quit): ")
    if topping == "quit":
        break
    print(f"Adding {topping}.")
