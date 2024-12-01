class Employee:
    def __init__(self):
        print("Constructive of Employee")
    person1 = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructive of Programmer")
    person2 = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructive of Manager")
    person3 = 3

# ans = Employee()
# print(ans.person1)

# ans = Programmer()
# print(ans.person1, ans.person2)

ans = Manager()
print(ans.person1, ans.person2, ans.person3)