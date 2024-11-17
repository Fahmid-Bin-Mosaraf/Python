def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter positive number: "))

print("Fibonacci Sequence: ")
for i in range(n):
    print(fibonacci(i))


"""
i=0 -> 0
i=1 -> 1
i=2 -> 1+0 -> 1
i=3 -> 1+1 -> 2
i=4 -> 2+1 -> 3

Sequence: 0 1 1 2 3
"""