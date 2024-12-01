class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = Number(100)
m = Number(250)

print(n+m)