"""
Write a program to print the following star pattern. 
* * * 
*   * 
* * *  
"""

n = int(input("Enter the number: "))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n, end="") # full row of *
    else:
        print("*", end="") # first * at the beginning of the row
        print(" "*(n-2), end="") # print n-2 space
        print("*", end="") # last * at the end of the row
    print("") # for newline

