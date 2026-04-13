lst = []

while True:
    i = int(input())
    if i == 0:
        break
    if i % 5==0:
        lst.append(i)

print(lst)
print(f'CNT: {len(lst)}')
print(f'HAP: {sum(lst)}')
print(f'AVG: {(sum(lst))/(len(lst)):.1f}')