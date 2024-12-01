class Employee:
    person = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of is {cls.person}")

e = Employee()
e.person = 50
e.show()