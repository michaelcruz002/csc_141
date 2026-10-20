
# 7-9 No Pastrami: Remove all pastrami orders before making food.

sandwich_orders = ["turkey", "pastrami", "tuna", "pastrami", "ham", "pastrami"]
finished_sandwiches = []

print("Sorry, we are out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("Sandwiches finished:")
for sandwich in finished_sandwiches:
    print(sandwich)
