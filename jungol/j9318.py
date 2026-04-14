lst = []
N = int(input())
for i in range(N):
    num = int(input())
    lst.append(num)
print(f'SUM: {sum(lst)}')
print(f'AVG: {sum(lst) // len(lst)}')