# Add a static method in problem 2, to greet the user with hello. 

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareRoot(self):
        print(f"The squareroot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello there!")

c = Calculator(10)
c.hello()
c.square()
c.cube()
c.squareRoot()