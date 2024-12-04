# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’. 


def divide(a, b):
    try:
        ans = a/b
        print(f"{a} / {b} = {ans}")

    except ZeroDivisionError:
        print("Infinite")

a = int(input("Enter (a): "))
b = int(input("Enter (b): "))

divide(a, b)