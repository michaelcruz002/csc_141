# Loop through a dictionary of rivers and countries.
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'mississippi': 'usa'}

for river, country in rivers.items():
    print("The", river, "runs through", country)

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)