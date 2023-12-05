# list, set, dictionary --> we're able to use comprehensions with these three data types.
# my_list = []
# for char in "hello":
# my_list.append(char)

my_list = [param for param in "hello"]
my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)
print(my_list3)
