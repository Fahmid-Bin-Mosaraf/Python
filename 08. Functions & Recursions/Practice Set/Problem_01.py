# Write a program using functions to find greatest of three numbers. 

def grestest(num1, num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

print(f"The greatest of the three number is: {grestest(num1, num2, num3)}")