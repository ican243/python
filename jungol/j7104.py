lst = []

for i in range(5):
    N = int(input())

    lst.append(N)


print(f'A = {lst}')

lst2 = lst[::-1]
print(f'B = {lst2}')


lst1 = lst[::-1]
A = int(input())
lst1.append(A)
print(f'C = {lst1}')

