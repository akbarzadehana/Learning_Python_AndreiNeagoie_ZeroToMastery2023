# Set
my_set = {1,2,3,4,5,5}
print(my_set)
my_set.add(6)
print(my_set)
print(len(my_set))
print(2 in my_set) 
#print(my_set[0])  # Set doesn't support indexing

my_list =[1,2,3,4,5,5]
print(set(my_list))

new_set = my_set.copy()
#my_set.clear()
#print(my_set)
print(new_set)

your_set = {4,5,6,7,8,9,10}
print(my_set.difference(your_set)) # It's going to find the difference of the first my_set with your_set. Just told you the difference without changing
print(your_set.difference(my_set))

print(my_set.discard(5))
print(my_set)

#my_set.difference_update(your_set)  # my_set will be modified because of difference.
print(my_set)

print(my_set.intersection(your_set))
print(my_set)

print(my_set.isdisjoint(your_set))

print(my_set.union(your_set))

print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))