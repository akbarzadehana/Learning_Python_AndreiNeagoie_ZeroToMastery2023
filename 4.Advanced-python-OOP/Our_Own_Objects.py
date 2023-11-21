# Attributes & Methods
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name="anonymous", age=0):
        if self.membership:  # or (PlayerCharacter.membership)
            # if (age > 18)
            # self refers to whatever's to the left of the dot.
            self.name = name
            self.age = age

    def run(self):
        print("run")
        return "Done1!"

    def shout(self):
        print(f"My name is {self.name}.")


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 22)
player2.attack = 50

# print(player1)
# print(player2)
# print(player1.run())
# print(player2.age)
# print(player2.attack)

print(player2.membership)
print(player1.shout())
