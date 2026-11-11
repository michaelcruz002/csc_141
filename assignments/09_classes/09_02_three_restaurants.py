
# 9-2 Three Restaurants: Create and describe three restaurants.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


restaurant1 = Restaurant("Pizza Palace", "Italian")
restaurant2 = Restaurant("Sushi House", "Japanese")
restaurant3 = Restaurant("Taco Place", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
