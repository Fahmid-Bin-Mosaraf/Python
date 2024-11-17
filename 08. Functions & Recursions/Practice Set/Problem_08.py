# Write a python function to print multiplication table of a given number.

def multiply(n):
    for i in range(1, n+1):
        print(f"{n}*{i} = {n*i}")

n = int(input("Enter a number: "))

multiply(n)


"""
5*1 = 5
5*2 = 10
5*3 = 15
5*4 = 20
5*5 = 25
"""