lst = []
while True:
    N = int(input())
    if N == -1:
        break
    lst.append(N)
my_list = lst[-3:]
print(*my_list)
    