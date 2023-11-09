# print(4 < 5)
# print(4 == 5)
# print(4=5)
# print("hello" == "hello")
# print("a" > "b")  # Why?
# print("a" > "A")
# print(1 < 2 < 3 > 4)
# print(1 >= 0)  # grater or equal
# print(0 != 0)  # not equal to
# print(not (True))
# print(not (1 == 1))

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician.")
elif is_magician and not is_expert:
    print("at least you're getting there.")
elif not is_magician:
    print("You need magic powers.")
