lst = []


while True:
    i = int(input())

    if i == 0:
        break
    lst.append(i)

A = (max(lst))
B = (min(lst))
print(f'MAX: {A}')
print(f'MIN: {B}')
