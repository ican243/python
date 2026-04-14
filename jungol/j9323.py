#num = int(input())
#num2 = int(input())
#if num > num2:
#        num, num2 = num2, num
#for i in range(num, num2 +1):
#    for j in range(1, 10):
#            print(f'{j} * {j} = {i * j:2d}', end = '   ')
#    print()


num = int(input())
num2 = int(input())
if num > num2:
        num, num2 = num2, num
for j in range(1, 10):       
    for i in range(num, num2 +1):
    
            print(f'{i} * {j} = {i * j}', end = '   ')
    print()
