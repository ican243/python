lst = []

for i in range(10):
    N = int(input())
    result = N % 42
    lst.append(result)
print(*lst, sep = '\n')