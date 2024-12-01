# Can you change the self-parameter inside a class to something else (say “fahmid”). Try changing self to “slf” or “fahmid” and see the effects.

class Example:
    def __init__(self, name):
        self.name = name 

    def display(self):
        print(f"Name is: {self.name}")

obj = Example("Fahmid")
obj.display()
