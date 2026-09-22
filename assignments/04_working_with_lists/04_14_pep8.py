# buffet.py
menu = ('pizza', 'pasta', 'salad', 'soup', 'steak')

# Print all menu items.
for food in menu:
    print(food)

# Tuples are immutable, so this will raise a TypeError.
try:
    menu[0] = "new value"
except TypeError:
    print("Sorry, the menu cannot be changed.")

# Create a new menu with an additional item.
new_menu = ('pizza', 'pasta', 'salad', 'soup', 'steak', 'dessert')

print()
print("The new menu includes:")
for food in new_menu:
    print(food)   