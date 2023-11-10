# iterpreter convert them to the same type
print(True == 1)
print("" == 1)
print("1" == 1)
print([] == 1)
print(10 == 10.0)
print(10 == 10)
print([] == [])
print([1, 2, 3] == [1, 2, 3])
print("**************")
# is actually check if the location in memory where this value is stoed, is the same.
print(True is 1)
print("" is 1)
print("1" is 1)
print([] is 1)
print(10 is 10.0)
print(10 is 10)
print(
    [] is []
)  # every time we create a list, it's added in memory somewhere. so these are two completely different.
print([1, 2, 3] is [1, 2, 3])
