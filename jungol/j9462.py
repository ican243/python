import random
N = int(input())
lst = list(map(int,input().split()))
for i in range(N-1):
    random.shuffle(lst)
    print(lst)