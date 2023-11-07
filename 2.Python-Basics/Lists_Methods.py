# Adding
Alphabet = ["a", "b", "c", "d"]
print(Alphabet)
Alphabet.append("e")  # Add to the end of the list
new_list = Alphabet[:]  # take a copy of Alphabet
Alphabet.append("f")
print(Alphabet)
print(new_list)
new_list.insert(5, "g")
print(Alphabet)
print(new_list)
new_list.insert(5, "f")
new_list.extend("hi")  # Notice!
print(new_list)

# Removing
Alphabet.pop()  # pop's off whatever is at the end of the list, returns whatever you have just removed.
print(Alphabet)
new_list.pop(0)  # pop's off whatever is at the index of the list, returns None.
print(new_list)
new_list.remove("b")
print(new_list)
new_list.clear()  # removes whatever is in the list, returns None.
print(new_list)

# Indexing
basket = [1, 2, 3, 4, 5]
print(basket.index(3, 0, 3))

# Search by keyword in python
print(1 in basket)
print(9 in basket)

user = "anahita"
print("a" in user)
print(user.count("a"))

# Sort
test_list = ["a", "b", "x", "d", "e", "c", "i"]
# (test_list.sort())  # Do it in place, returns None
print(sorted(test_list))  # pro duces a new one, doesn't modify the list in place.
print(test_list)  # hasn't been modified.
# new_test = test_list.copy()  # Do the same as new_test = test_list[:]
test_list.reverse()  # Do it in place and switching all the indexes into opposite sides.
print(test_list)
# If you want a sorted, reversed list first .sort() and then .reverse()
print(list(range(10, 21)))

# common List patterns
basket = ["a", "x", "b", "c", "d", "e", "d"]
basket.sort()
basket.reverse()
# print(basket[::-1])
# print(basket[:])
# print(basket)

# range
print(range(1, 100))
print(range(20))
print(list(range(1, 20)))

# join
sentence = "!"
new_sentence = sentence.join(["Hi", ",", "my", "name", "is", "Ana", "."])
# new_sentence = " ".join(["Hi", ",", "my", "name", "is", "Ana", "."])
print(new_sentence)

# List Unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
