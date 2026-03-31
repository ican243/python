list = []

for i in range(5):
    num = int(input())
    list.append(num)

for i in list:
    print(i, end = ' ') #기본 활용 

print(*list)      #// 언패킹  * 활용용

