lst = []
lst2 = []

while True:
    i = int(input())
    if i == 0:
        break
    elif i % 2 == 1:
        lst.append(i)
    else:
        lst2.append(i)


print(f'odd = {lst}')
print(f'even = {lst2}')

