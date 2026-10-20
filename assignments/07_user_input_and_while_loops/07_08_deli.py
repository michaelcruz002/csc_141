
# 7-8 Deli: Make sandwiches and move them to a finished list.

sandwich_orders = ["turkey", "tuna", "ham"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("Sandwiches finished:")
for sandwich in finished_sandwiches:
    print(sandwich)
