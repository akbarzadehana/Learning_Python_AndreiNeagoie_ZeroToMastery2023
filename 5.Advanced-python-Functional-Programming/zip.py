# We need two lists or two iterables and we can zip them together.
my_list = [1, 2, 3]
your_list = (10, 20, 30)
their_list = [5, 4, 3]

print(list(zip(my_list, your_list, their_list)))
print(my_list)
