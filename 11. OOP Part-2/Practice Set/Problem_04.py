# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.


class Complex:
    def __init__(self, real, imag):
        # Complex number with real and imaginary parts.
        self.real = real  
        self.imag = imag

    def __add__(self, other):
        # Add two complex numbers.
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        # Multiply two complex numbers.
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __str__(self):
        # Returns a string representation of the complex number.
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

c1 = Complex(3, 2)  
c2 = Complex(1, 7) 

# Add complex numbers
sum_result = c1 + c2
print(f"Sum: {sum_result}") 

# Multiply complex numbers
mul_result = c1 * c2
print(f"Multiplication: {mul_result}")  
