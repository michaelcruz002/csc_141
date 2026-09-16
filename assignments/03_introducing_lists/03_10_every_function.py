cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

print(f"The number of cities in the list is {len(cities)}")

cities.sort()

print(f"The sorted cities list is: {cities}")

reversed_cities = sorted(cities, reverse=True)

print(f"The reversed sorted cities list is: {reversed_cities}")

cities.reverse()

print(f"The reversed sorted cities list is: {cities}")

removed_element = cities.pop()

print(f"The removed city element is: {removed_element}")