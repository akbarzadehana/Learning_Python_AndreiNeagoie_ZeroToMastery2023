first_name = "Anahita"
last_name = "Akbarzadeh"
# print(first_name + " " + last_name)
# print(f"Hi {first_name} {last_name}")  # This is a new feature for Python 3
# print("Hi {0} {1}".format(first_name, last_name))
# print("Hi {name} {last }".format(name="Mohammad", last="Hamidi"))
test_string = "0123456789"
print(test_string[-2:-11:-2])
# test_string[10] = "0"  # You can't reassign part of a string.
test_string = "0123456780"
print(test_string)
print(len(test_string))
print(test_string[0 : len(test_string)])
print(first_name.capitalize())
print(first_name.upper(), last_name.upper())
print(first_name.find('ah'))
print(first_name.replace("ah", ""))
print(first_name)
first_name = first_name.replace("ah", "")
print(first_name)
