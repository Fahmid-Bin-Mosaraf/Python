def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter a number: "))
print(f"The factorial of this number is : {factorial(n)}")


"""
n = 5
5*(5-1) -> 5*4
5*(4-1) -> 5*4*3
5*(3-1) -> 5*4*3*2
5*(2-1) -> 5*4*3*2*1 = 120
"""