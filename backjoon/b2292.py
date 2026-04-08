# N = int(input())


# if N == 1:
#     print('1')
# elif 2 <= N <= 7:
#     print('2')
# elif 8 <= N <= 19:
#     print('3')
# elif 20 <= N <= 37:
#     print('4')
# else:
#     print('5')



N = int(input())

total = 1
count = 1

while N > total:
    total += count * 6
    count += 1

print(count)

