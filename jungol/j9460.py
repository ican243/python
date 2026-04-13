def change(x, y):
    x, y = y, x
    print(f'함수 내부: a = {x}, b = {y}')

a, b = map(int, input().split())

change(a, b)
print(f'함수 외부: a = {a}, b = {b}')

change(a, b)
a, b = b, a
print(f'함수 외부: a = {a}, b = {b}')