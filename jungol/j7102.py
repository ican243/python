lst = []
total = 0
N = int(input())
for i in range(N):
    a = int(input())
    if a % 2 == 1:
        total += a
    else:
        lst.append(a)
print(f'{total} {len(lst)}')

