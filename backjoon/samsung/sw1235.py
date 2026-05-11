lst = []
lst2 = []
lst3 = []

for i in range(8):
    a = int(input())
    lst.append(a)
    lst2 = lst[0:5]
    lst3 = list(reversed(lst2))
    
print(lst3)
print(lst)
print(lst2)