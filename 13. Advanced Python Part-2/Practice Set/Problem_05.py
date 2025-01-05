#  Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
numbers = [2, 7, 1, 5, 22, 20, 18, 15, 35, 25, 10]

def greatest(a, b):
    if(a>b):
        return a
    return b

print(reduce(greatest, numbers))