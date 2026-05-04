N = int(input())
num = list(map(int,input().split()))

for i in range(N - 1):
    one = i
    for j in range(i + 1, N):
        if num[j] < num[one]:
            one = j
        
    num[i], num[one] = num[one], num[i]
    
    print(num)
            



