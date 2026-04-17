N = int(input())
for i in range(N):
    num = input()
    total = 0
    case = 0
    for j in num:
        if j == 'O':
            case += 1
            total += case
        else:
            case = 0
    print(total)

    