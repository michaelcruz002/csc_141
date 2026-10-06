# Add a new item to an existing dictionary and loop through it.
favorite_numbers = {'sonic': 1, 'tails': 2}

favorite_numbers['knuckles'] = 3

for person, number in favorite_numbers.items():
    print(person, "likes", number)