class Day:
    def __init__(self, year, price):
        self.year = year
        self.price = price

    def how(self, Y, P):
        if self.year >= Y and self.price <= P:
            print(self.year, self.price)

N = int(input())

day = []

for i in range(N):
    y, p = map(int,input().split())
    day.append(Day(y, p))

y, p = map(int,input().split())

for b in day:
    b.how(y, p)


class Day:
    def __init__(self, year, price):
        self.year = year
        self.price = price

    def hwo(self, X, Y):
        if self.year >= X and self.price <= Y:
            print(self.year, self.price)

N = int(input())

day = []

for i  in range(N):
    x, y = map(int,input().split())
    day.append(Day(x, y))

for b in day:
    b.how(x, y)