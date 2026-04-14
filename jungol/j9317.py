lst = []

N = int(input())
for i in range(5, N+1, 5):
    lst.append(i)
print(*lst)
print(sum(lst))

    