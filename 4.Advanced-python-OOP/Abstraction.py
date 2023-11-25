# Abstraction means hiding of information or abstracting away information and giving access to only what's necessary.
# there is no true private variables. We use _ to say other programmer that please don't change it.
class PlayerCharacter:
    def __init__(self, name, age):
        # please don't toch this
        self._name = name
        self._age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"My name is {self._name}, I am {self._age} years old.")


player1 = PlayerCharacter("andrei", 100)
# player1._name = "!!!"
# player1.speak()= "Booo"

print(player1._name)
