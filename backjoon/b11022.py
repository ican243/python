N = int(input())
for i in range(1,N+1):
    a, b = map(int,input().split())
    print(f'Case #{i}: {a} + {b} = {a + b}')

    total = 0
N = int(input())
for i in range(N):
    num = input()
    if num == 'o':
        total += num
    elif num == 'oo':
        total += num
    elif num == 'ooo':
        total += num
    elif num == 'oooo':
        ltotal += num
    elif num == 'ooooo':
        total += num
    elif num == 'oooooo':
        total += num
print(total)
    