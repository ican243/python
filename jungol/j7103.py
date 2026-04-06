lst = []
lst2 = []
lst3 = []

for i in range(8):
    N = int(input())
    lst.append(N)
    lst2.append(N)
    lst3.append(N)
del lst2[5:]
del lst3[5:]
lst3.reverse()
print(lst3)
print(lst)
print(lst2)

print('-----------')

lst = []

for i in range(8):
    N = int(input())
    lst.append(N)

lst2 = lst[:5]
lst3 = lst[5:]
lst3.reverse()

print(lst)
print(lst2)
print(lst3)




