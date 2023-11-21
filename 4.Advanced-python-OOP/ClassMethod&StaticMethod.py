class PlayerChracter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"My name is {self.name}.")

    # we can usually use this without even instantiating a class.
    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


# player1 = PlayerChracter("Tom", 20)
player3 = PlayerChracter.adding_things(2, 3)
print(player3.age)
