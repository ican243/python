N = int(input())

for i in range(N, 0, -1):
    for j in range(5, 0, -1):
        if i >= j:
            print("*", end = '')
    print()



# ------------------------------------------
n = int(input())
for i in range(n,0,-1):
    print('*'*i)


#------------------------------------------------
N = int(input())
stars = "*" * N

for i in range(N):
    print(stars[:N - i])
