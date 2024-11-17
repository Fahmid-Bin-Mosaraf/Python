# Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*9/5)+32
    return fahrenheit

celsius = int(input("Enter temperature in celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")


"""
(100*9/5)+32
= 100*1.8+32
= 212.0 °F
"""