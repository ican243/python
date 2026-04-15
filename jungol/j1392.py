lst = []

for i in range(7):
    N = int(input())
    if N % 2 == 1:
        lst.append(N)
if len(lst) == 0:
        print(-1)
else:
    print(sum(lst))
    print(min(lst))
