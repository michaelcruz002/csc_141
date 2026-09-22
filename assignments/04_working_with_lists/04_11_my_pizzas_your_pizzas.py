
pizzas = ['Margherita', 'Pepperoni', 'Hawaiian', 'Veggie', 'BBQ Chicken']

friend_pizzas = pizzas[:]

pizzas.append('Mushroom')
friend_pizzas.append('Sausage')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)