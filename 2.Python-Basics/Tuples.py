# Tuple : Immutable list
my_tuple = (1,2,3,4,5)
#my_tuple[0] = 'a'
print(my_tuple[0])
print(2 in my_tuple)

test = {(1,2) : "a", "Greet": "Hey"}
print(test[(1,2)])

copy_tuple = my_tuple[1:2]
print(copy_tuple)

x,y,z,*other = my_tuple # It assigns rest of the items to the other as a list.
print(other) 

print(my_tuple.count(1))
print(my_tuple.index(1)) # It returns the index of first same value to the argument that finds.
print(len(my_tuple))
