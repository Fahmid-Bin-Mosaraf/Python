"""
Write a program to print the following star pattern. 
  * 
 *** 
*****
"""

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "*(n-i), end="") # for space
    print("*"*(2*i-1),end="") # for *
    print("") # for newline 