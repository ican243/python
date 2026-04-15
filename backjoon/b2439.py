# N = int(input())

# for i in range(N):
#     for j in range(N):
#         if j < N - i -1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

a=int(input())
for i in range(1,a+1):
    print((i*"*").rjust(a))
