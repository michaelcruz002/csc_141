# Loop through a dictionary of words and print them.
glossary = {
    'string': 'A series of characters',
    'list': 'Items in an order',
    'loop': 'Working through items',
    'dictionary': 'Key-value pairs',
    'print': 'Shows text on the screen'
}

for word, meaning in glossary.items():
    print(word, "-", meaning)