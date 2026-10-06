# Store lists of favorite places in a dictionary.
places = {
    'sonic': ['green hill', 'studiopolis'],
    'tails': ['mystic ruin', 'emerald coast']
}

for person, user_places in places.items():
    print(person, "likes these places:")
    for place in user_places:
        print(place)