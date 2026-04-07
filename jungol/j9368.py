lst = []
N = int(input())

for i in range(N):
    S = int(input())
    lst.append(S)
    lst.sort(reverse = True)

print(lst)

