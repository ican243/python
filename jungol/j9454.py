# x, y = map(int, input().split())

# def plus():
#     print(f'두 수의 합 = {x+y}')
# def minus():
#     print(f'두 수의 차 = {y-x}')
# plus()
# ()



x, y = map(int, input().split())

def plus(x, y):
    return x + y

def minus(x, y):
    return abs(x - y)

print("두 수의 합 =", plus(x, y))
print("두 수의 차 =", minus(x, y))