# Check if people took a poll using a dictionary.
favorite_languages = {'jen': 'python', 'sarah': 'c'}

people = ['jen', 'sarah', 'sonic', 'tails']

for person in people:
    if person in favorite_languages.keys():
        print(person, "thank you for taking the poll")
    else:
        print(person, "please take the poll")