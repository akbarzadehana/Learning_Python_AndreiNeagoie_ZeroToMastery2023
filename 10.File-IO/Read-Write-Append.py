# a better way to actually do file IO with python is with the built in with statements.
with open("WriteMode.txt", mode="r+") as my_file:
    text = my_file.write("This is a test to write with python in file!")
    print(text)
# when we open a file the cursor goes to zero.
with open("WriteMode.txt", mode="a") as my_file:
    text = my_file.write(":)")
    print(text)
# in write mode ("w"), it will assume this is a new file and we just want to add the smiley face.
# so be careful that you use the right mode based on what you need.

with open(
    "sad.txt", mode="w"
) as my_file:  # write also creates a new file if it doesn't exist already or overwrites the existing one.
    text = my_file.write(":(")
    print(text)
