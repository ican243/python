total = 0

a, b = map(int,input().split())

if a > b:
    a, b = b, a

for i in range(a+1, b+1, 2):
    total += i
print(total)