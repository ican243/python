# N = int(input())

# for i in range(N):
#     a, b = input().split()   
#     for x in range(len(b)):
#         print(b[x]*int(a), end = '')
#     print()


#-----------------


# N = int(input())

# for i in range(N):
#     a, b = input().split()   
#     for i in b:
#         for j in range(int(a)):
#             print(i, end = '')      
#     print()
 

# T = int(input())
# lstr = []
# lsts = []

# for n in range(T):                           ----교수니꺼 복수하기 깃허브 백준꺼 확인 
#     R, S = input().split()   
#     lstr.append(int(a))
#     lsts.append(b)
# for m in range(len(lstr)):
#     print(lstr[m], lsts[m])
#     for j in range(int(a)):
#         print(i, end = '')      
#     print()

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for x in S:
        print(x*R, end='')
    
    print()