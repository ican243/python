N = int(input())
for i in range(1, N+1):
    a = int(input())
    lst = list(map(int,input().split()))
    result = max(lst) - min(lst)
    print(f'#{i} {result}')
