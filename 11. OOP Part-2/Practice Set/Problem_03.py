# Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.increment = 0 
 
    # Apply the increment to the employee's salary
    def apply_increment(self):
        if self.increment > 0:
            self.salary += self.salary * (self.increment/100)
        else:
            print("No increment applied.")

    # Employee details including name, salary, and increment percentage
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Current Salary: {self.salary:.2f}")
        print(f"Increment Percentage: {self.increment}%")

emp = Employee("Fahmid", 50000) # initial details
emp.display_details()

emp.increment = 10 # inrement 10%
emp.apply_increment() # apply for inrement
emp.display_details()


