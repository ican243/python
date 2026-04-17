a, b, c = map(int,input().split())

if a == b and a != c and b != c:
    print(f'{1000 + (a * 100)}')
elif a == c and a != b and b != c:
    print(f'{1000 + (a * 100)}')
elif b == c and a != b and a != c:
    print(f'{1000 + (b * 100)}')
elif a == b == c:
    print(f'{10000 + (a * 1000)}')
elif a > b and a > c:
    print(f'{a * 100}')
elif b > a and b > c:
    print(f'{b * 100}')
elif c > a and c > b:
    print(f'{c * 100}')