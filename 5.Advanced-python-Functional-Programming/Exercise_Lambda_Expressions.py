# Square
my_list = [5, 4, 3]
print(list(map(lambda item: item * item, my_list)))

# List Sorting
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
# a.sort()    it will sort by the first item in tuple
a.sort(key=lambda x: x[1])
print(a)
