
# 9-6 Ice Cream Stand: Inherit from Restaurant and list flavors.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, "ice cream")
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)


stand = IceCreamStand("Sweet Treats")
stand.describe_restaurant()
stand.show_flavors()
