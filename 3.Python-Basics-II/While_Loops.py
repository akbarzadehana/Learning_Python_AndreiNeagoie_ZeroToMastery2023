i = 0
while i < 20:
    print(i)
    i += 1
    # break     the else block execute if there isn't a break statement
else:
    print("Done with all the work!")

my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input("say something: ")
    if response == "bye":
        break

# break & continue keyword works in a for loop as well.
i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i])

print("Done!")

for item in my_list:
    # thinking about it
    pass  # Hey, I'm thinking about it. I'm just going to pass it for now
