class Employee:
    company = "Google"
    salary = 100000

    def getSalary(self):
        print(f"The company name is {self.company}. The salary is {self.salary}.")

google = Employee()
google.getSalary()