# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p1 = Programmer("Fahmid", 12000, 20011)
p2 = Programmer("Famel", 12000, 20012)
p3 = Programmer("Rabi", 12000, 20013)

print(p1.company, p1.name, p1.salary, p1.pin)
print(p1.company, p2.name, p2.salary, p2.pin)
print(p1.company, p3.name, p3.salary, p3.pin)
