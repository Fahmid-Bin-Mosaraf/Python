#  Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    # vector x, y, z
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # add two vectors
    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    # calculate the dot product of two vectors
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    # display vector as string
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9) 

print(v1 + v2)  # addition
print(v1 * v2)  # dot product
print(v1 + v3)  # vector addition with another vector
print(v1 * v3)  # dot product with another vector  