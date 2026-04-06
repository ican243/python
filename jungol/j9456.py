# a, b, c = map(int,input().split())


# def num(x):
#     print(a*x**2 + b*x + c)

# num(2)
# num(3)
# num(5)



a, b, c = map(int,input().split())

def func(x, a, b, c):
    res = a * x * x + b * x + c
    return res

print(func(2, a, b, c))
print(func(3, a, b, c))
print(func(5, a, b, c))