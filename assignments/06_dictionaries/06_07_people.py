# Store dictionaries of people inside a list.
person_1 = {'name': 'sonic', 'age': 15}
person_2 = {'name': 'tails', 'age': 8}
person_3 = {'name': 'knuckles', 'age': 16}

people = [person_1, person_2, person_3]

for person in people:
    print(person['name'], "is", person['age'])