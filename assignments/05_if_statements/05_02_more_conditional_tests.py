number = 10

print("Is >= 10 AND even? I predict True.")
print(number >= 10 and number % 2 == 0)
print("Is number >=10 ANd odd? I predict False.")
print(number >= 10 and number % 2 != 0)

print("Is number >=10 ANd odd? I predict True.")
print(number >= 10 or (number % 2 != 0))

list_1 = ["Michael", "Alice"]

print("Is 'Paul' in list_1? I predict False.")
print("Paul" in list_1)
print("Is 'Michael' in list_1? I predict True.")
print("Michael" in list_1)

print("Is 'Michael' not in list_1? I predict False.")
print("Michael" not in list_1)