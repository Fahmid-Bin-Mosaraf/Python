#  Write a program to filter a list of numbers which are divisible by 5.

def divisibles_by_5(n):
    if(n%5 == 0):
        return True
    return False

numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

div = list(filter(divisibles_by_5, numbers))
print(div)



