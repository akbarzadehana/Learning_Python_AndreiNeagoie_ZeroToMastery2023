# Exercise: Check for duplicates in list:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
Duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in Duplicates:
            Duplicates.append(value)
print(Duplicates)
