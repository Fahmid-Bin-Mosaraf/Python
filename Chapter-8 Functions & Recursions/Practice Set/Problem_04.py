#  Write a recursive function to calculate the sum of first n natural numbers. 

def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)
    
n = int(input("Enter a positive number: "))

print(f"The sum is: {sum(n)}")



"""
n = 5
5+(5-1) -> 5+4
5+(4-1) -> 5+4+3
5+(3-1) -> 5+4+3+2
5+(2-1) -> 5+4+3+2+1 = 15
"""