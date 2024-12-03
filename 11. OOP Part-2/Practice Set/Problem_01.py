#  Create a class (2-D vector) and use it to create another class representing a 3-D vector. 

# 2D Vector
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is: {self.i} + {self.j}")
        
# 3D Vector, inheriting form 2D Vector
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        # initialize the k 
        self.k = k

    def show(self):
        print(f"The vector is {self.i} + {self.j} + {self.k}")

a = TwoDVector(1, 2)
a.show()

b = ThreeDVector(5, 2, 3)
b.show()