lst = []

for i in range(5):
    N = int(input())
    lst.append(N)

x = lst[::2]


print(lst)
print(*x)

