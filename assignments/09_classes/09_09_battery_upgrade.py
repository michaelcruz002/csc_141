
# 9-9 Battery Upgrade: Upgrade a car battery and compare its range.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Battery size: {self.battery_size} kWh")

    def get_range(self):
        if self.battery_size == 40:
            print("This car can go about 150 miles.")
        else:
            print("This car can go about 225 miles.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_car = ElectricCar("Nissan", "Leaf", 2024)
print(my_car.get_descriptive_name())
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()
