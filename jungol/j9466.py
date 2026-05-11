def drow(n):
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end=' ')
            num += 1
        print()

N = int(input())

drow(N)
   


