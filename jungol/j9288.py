total = 0
count = 0

while True:
    N = int(input())

    if N == 0:
        break
    total += N
    count += 1

print(f'cnt = {count}')
print(f'sum = {total}')