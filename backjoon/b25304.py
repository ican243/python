total = int(input())
N = int(input())
lst = []

for i in range(N):
    a, b = map(int,input().split())
    plus = (a * b)
    lst.append(plus)
    
if sum(lst) == total:
    print('Yes')
else:
    print('No')
