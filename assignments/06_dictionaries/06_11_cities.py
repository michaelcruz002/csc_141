# Store information about cities in nested dictionaries.
cities = {
    'station square': {'country': 'united federation', 'pop': 2000000},
    'spagonia': {'country': 'earth', 'pop': 5000000}
}

for city, info in cities.items():
    print("City:", city)
    print("Country:", info['country'])
    print("Population:", info['pop'])