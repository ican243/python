# N = int(input())
# i = 1
# total = 0
# while i <= N:
#     total += i
#     i += 1
# print(total)

N = int(input())

for i in range(1, N+1):
    if i % 2 == 0:
        print(i, end=" ")