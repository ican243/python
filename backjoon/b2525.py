a, b = map(int, input().split())
N = int(input())

b = b + N

a = a + (b // 60)
b = b % 60

if a >= 24:
    a = a % 24

print(a, b)


