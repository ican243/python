lst = []

for i in range(5):
    N = int(input())

    lst.append(N)
    lst1 = lst[2:]
    lst2 = lst[2:][::-1]
    lst3 = lst[::-1]
print(lst1)
print(lst2)
print(lst3)