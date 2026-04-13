

lst = []

while True:
    n = int(input())
    
    if n == -1:
        break

    lst.append(n)

print(*lst[-3:])