class Employee:
    person1 = 1

class Programmer(Employee):
    person2 = 2

class Manager(Programmer):
    person3 = 3

ans = Employee()
print(ans.person1)

ans = Programmer()
print(ans.person1, ans.person2)

ans = Manager()
print(ans.person1, ans.person2, ans.person3)