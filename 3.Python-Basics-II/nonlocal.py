# the nonlocal keyword is used to refer to parent local.
# Hey, I want to use a variable that is not a global variable but is outside of the scope of my function.
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
