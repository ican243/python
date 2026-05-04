for i in range(1, 4):
    print(' ' * (3 - i) + '*' * i)


for i in range(1, 4):
    for j in range(3 - i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()    