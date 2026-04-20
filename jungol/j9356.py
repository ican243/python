lst = []
lst = list(map(int, input().split()))
lst_item = lst.pop(4)
print(f'last: {lst_item}')
print(lst)
print(f'len: {len(lst)}')

lst2 = []
lst2 = list(map(int, input().split()))
lst_item2 = lst2.pop(1)
print(f'second: {lst_item2}')
print(lst2)
print(f'len: {len(lst2)}')



lst = []
for i in range(1, 6):
    lst.append(i)
b = lst.pop(4)
a = len(lst)
print(f'last: {b}')
print(lst)
print(f'len: {a}')

lst2 = []
for i in range(1, 5):
    lst2.append(i)
b2 = lst2.pop(1)
a2 = len(lst2)
print(f'second: {b2}')
print(lst2)
print(f'len: {a2}')