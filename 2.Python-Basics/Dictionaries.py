# Dictionary
dictionary = {"a": [1, 2, 3], "b": "Hi", "c": True}
print(dictionary)

my_list = [
    {"a": [1, 2, 3], "b": "Hi", "c": True},
    {"a": [4, 5, 6], "b": "By", "c": False},
]
print(my_list[1]["a"][0])

# Dictionary Keys : A key needs to be immutable, and can not change. numbers, strings, booleans can be key but not lists.
my_dictionary = {
    1: ["a", "b", "c"],
    1: "It's me!",
}  # The value of a key should be uniqe, so list doesn't exist anymore.
print(my_dictionary[1])
