# TODO: dictionary with values
inventory = {
  'gold': 500,
  'pouch': ['flint', 'twine', 'gemstone'],
  'backpack': ['xylophone', 'dagger', 'bedroll', 'breadloaf']
}

# TODO: add key_pocket and values to dictionary
inventory["pocket"] = ['seashell', 'strange berry', 'lint']

# TODO: ( .sort()) elements in backpack and print
inventory['backpack'].sort()

print(inventory)

# TODO: del dagger from list
inventory['backpack'].remove('dagger')

# TODO: add 50 gold and print results
inventory['gold'] += 50

print(inventory)
