# Parameters   parameters are used when we define the function.
# Default Parameters
def say_hello(name="Darth", emoji="._."):
    print(f"Hello {name} {emoji}")


# Positional arguments are arguments that require to be in the proper position.
# Arguments    arguments are used as the actual values we provide to a function, used when we call the function.
say_hello("Anahita", ":)")


# Keyword arguments, not worry about the position.
say_hello(emoji=":)", name="Ana")

say_hello()
say_hello("Mohammad")
