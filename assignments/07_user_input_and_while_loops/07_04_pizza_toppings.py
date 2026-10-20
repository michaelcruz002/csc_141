
# 7-4 Pizza Toppings: Keep asking for toppings until the user quits.

while True:
    topping = input("Enter a pizza topping (or quit): ")
    if topping == "quit":
        break
    print(f"I will add {topping} to your pizza.")
