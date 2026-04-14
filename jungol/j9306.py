lst = []
N = int(input())
for i in range(N):
    num = int(input())
    lst.append(num)
print(f'sum: {(sum(lst))}')
print(f'avg: {(sum(lst)) / (len(lst))}')