# iterable - list, dictionary, tuple, set, string.
# iterate -> one by one check each item in the collection.
user = {"name": "Ana", "age": 27, "can_swim": True}

for item in user.items():
    print(item)
for item in user.values():
    print(item)
for item in user.keys():
    print(item)

for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)
