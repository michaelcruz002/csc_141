# Store multiple favorite numbers in a dictionary.
numbers = {
    'sonic': [1, 7],
    'tails': [2, 8]
}

for person, nums in numbers.items():
    print(person, "likes these numbers:")
    for num in nums:
        print(num)