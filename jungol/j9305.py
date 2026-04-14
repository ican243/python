lst = []
lst2 = []
N = int(input())
for i in range(N):
    num = int(input())
    if num % 2 == 0:
        lst.append(num)
    if num % 3 == 0:
        lst2.append(num)
print(f'2의 배수: {len(lst)}')
print(f'3의 배수: {len(lst2)}')