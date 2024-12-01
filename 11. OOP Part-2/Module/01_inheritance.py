class Employee:
    company = "Google"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company = "Microsoft"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

e1 = Employee()
e2 = Programmer()

print(e1.company, e2.company)