
# 9-5 Login Attempts: Count user logins and reset the count.
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} lives in {self.city}.")

    def greet_user(self):
        print(f"Welcome, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Alex", "Smith", 18, "Newark")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print("Login attempts:", user.login_attempts)

user.reset_login_attempts()
print("After reset:", user.login_attempts)
