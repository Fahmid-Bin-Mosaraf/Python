class Footballer:
    # class attribute
    attribute = "GOAT"

    # instance attribute
    def __init__(self, name):
        self.name = name

# object instantiation
Ronaldo = Footballer("Ronaldo")
Messi = Footballer("Messi")


# accessing class attributes
print("Ronaldo is a {}".format(Ronaldo.__class__.attribute))
print("Messi is also a {}".format(Messi.__class__.attribute))

# accessing instantiation attributes
print("My name is {}".format(Ronaldo.name))
print("My name is {}".format(Messi.name))