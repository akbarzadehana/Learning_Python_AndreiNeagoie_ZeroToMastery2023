# the idea of encapsulation, encapsulation is the binding of data and functions that manipulate that data.
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"My name is {self.name}, I am {self.age} years old.")


player1 = PlayerCharacter("andrei", 100)
player1.speak()
