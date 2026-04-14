lst = []
a, b = map(int,input().split())
if a > b:
            a, b = b, a   
for i in range(a, b+1):
    if i % 3 == 0 or i % 5 == 0:     
        lst.append(i)
print(f'CNT: {len(lst)}')
print(f'SUM: {sum(lst)}')