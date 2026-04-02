total = 0
count = 0

while True:
    N = int(input())
    if N == 0:
        break
    if N < 1 or N > 100:
        continue
    total += N
    count += 1

avg = (total // count)
print(f'count = {count}')
print(f'total = {total}')
print(f'avg = {avg}')