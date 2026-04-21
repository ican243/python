while True:
    a, b = map(int, input().split())

    if (a > 9 or a < 2) or (b > 9 or b < 2):
        print('INPUT ERROR!')
    else:
        break
if a < b:
    go = 1
    num = b + 1
else:
    go = -1
    num = b - 1

for j in range(1, 10):
    for i in range(a, num, go):
        
        print(f'{i} * {j} = {(i * j):2d}', end = '   ')
    print()