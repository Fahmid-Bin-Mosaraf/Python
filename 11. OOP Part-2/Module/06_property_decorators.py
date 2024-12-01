class Employee:
    person = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.person}")

    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.person = 50

e.name = "Fahmid Bin Mosaraf"
print(e.fname, e.lname)

e.show()