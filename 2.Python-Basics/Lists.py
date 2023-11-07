Shopping_List = ["Backpack", "Shoes", "Clothes for Gym"]
print(Shopping_List)
print(Shopping_List[0:2])
Shopping_List[2] = "Air Pods"
print(Shopping_List)  # Lists are mutable, it doesn't nessecery to overwrite all part.
# New_list = Shopping_List  # any change in New_list will change the Shopping_List and conversely
New_list = Shopping_List[:]  # We just take a copy of Shopping_List
Shopping_List[1] = "Hiking Shoes"
print(Shopping_List)
print(New_list)
New_list[0] = "Tote Bag"
print(New_list)
print(Shopping_List)

