N = int(input())
for i in range(1, N+1):
    lst = list(map(int,input().split()))

    total = 0

    for j in lst:
        if j % 2 == 1:
            total += j
    print(f'#{i} {total}')

