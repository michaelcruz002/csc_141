
menu = ('pizza', 'pasta', 'salad', 'soup', 'steak')

for food in menu:
    print(food)

try: 
    menu[0] = "new value"
except TypeError:
    print("Sorry, the menu cannot be changed.")

new_menu = ('pizza', 'pasta', 'salad', 'soup', 'steak', 'dessert')
print("The new menu includes:")
for food in new_menu:
    print(food)