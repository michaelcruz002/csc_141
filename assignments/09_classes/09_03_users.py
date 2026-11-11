
# 9-3 Users: Create users and print their information.
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, age {self.age}, lives in {self.city}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


user1 = User("Alex", "Smith", 18, "Newark")
user2 = User("Jordan", "Lee", 19, "New York")
user3 = User("Sam", "Brown", 20, "Boston")

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()
