K = int(input())
a, b, c = map(int,input().split())

def like(N):
    return(abs(K - N))

print(like(a))
print(like(b))
print(like(c))
