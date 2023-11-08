# Dictionary Methods
user = {"basket": [1, 2, 3], "greet": "Hello", "age": 20}
# print(user["age"])  # We need a way to avoid these errors.
# print(user.get("age", 20))  # If dictionary doesn't have this key just returns None. In this case we set a default value.

# Another way to create a dictionary
user2 = dict(name="Anahita")
print(user2)
print("name" in user2)  # It will check both keys and values
# print("basket" in user.keys())
# print("Hello" in user.values())
print(user.items())

# Remove
user2.clear()  # It returns None.
print(user2)  # In place removes whatever the dictionary


# copy
copy_user = user.copy()  # Do not copy in place.
# print(user.clear())
# print(copy_user)

# pop
# print(user.pop('greet'))       # Notice that pop expected at least 1 argument, in this case should be one of the keys.
# print(user)

# popitem
# print(user.popitem())
# print(user)

# update
print(
    user.update({"age": 55})
)  # we could update the dictionary with a key that we didn't have before.
print(user)
