N = int(input())
for i in range(1, N+1):
    for j in range(N):
        a = i + (j * N)
        print(a, end=' ')
    print()
