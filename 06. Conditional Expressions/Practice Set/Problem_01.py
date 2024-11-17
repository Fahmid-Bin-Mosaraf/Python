# Write a program to find the greatest of four numbers entered by the user.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num2) & (num1>num3) & (num1>num4):
    print(f"Greateste number is num1: {num1}")

elif(num2>num1) & (num2>num3) & (num2>num4):
    print(f"Greateste number is num2: {num2}")

elif(num3>num1) & (num3>num2) & (num3>num4):
    print(f"Greateste number is num3: {num3}")
    
else:
    print(f"Greateste number is num4: {num4}")
