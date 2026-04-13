lst = []
lst2 = []

a, b = map(int,input().split())
a2, b2 = map(int,input().split())
lst = [a]*b
lst2 = [a2]*b2

# print(lst)
# print(lst2)
result = lst + lst2
print(result)