# when we do something like User, it's actually accepting object as the parent.
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):
        print("Do nothing")


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self)
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")


wizard1 = Wizard("Merlin", 50, "Merlin@gmail.com")
archer1 = Archer("Robin", 100)
wizard1.attack()

# Check if something is an instance of a class
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))

# Everything in python is an object.
print(isinstance(wizard1, object))


# Polymorphism
def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

print(wizard1.email)
