# Store dictionaries about pets in a list.
pet_1 = {'animal': 'chao', 'owner': 'cream'}
pet_2 = {'animal': 'fox', 'owner': 'tails'}
pet_3 = {'animal': 'echidna', 'owner': 'knuckles'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(pet['owner'], "has a", pet['animal'])