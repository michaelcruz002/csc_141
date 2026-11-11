
# 9-1 Restaurant: Create a class to represent a restaurant.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range

        def describe_restaurant(self):
            print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant located at {self.location} with a price range of {self.price_range}.")
            print (f'The price range is {self.price_range}.')

            def can_you_take_a_date(self):
                if self.price_range >= 50:
                    print(f"Don't embarass yourself. It's too expensive!")
                else:
                    print(f'You can afford {self. restaurant_name}.')

                cici_place = Restaurant ('Cici Shack', 'Soul food', 'Philiadelphia', 50)
                cici_place.describe_restaurant()
                cici_place.can_you_take_a_date()