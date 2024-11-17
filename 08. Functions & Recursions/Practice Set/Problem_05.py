"""
Write a python function to print first n lines of the following pattern: 
*** 
**               
* 
"""

def pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

n = int(input("Enter the number of lines: "))

pattern(n)


"""
for n=3
The loop starts from n=3 and decreases by 1 each iteration
i=3 -> ***
i=2 -> **
i=1 -> *
"""