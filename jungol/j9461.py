def num(x, y):
    global a, b
    if x > y:
        a = x // 2
        b = y * 2
    else:
        a = x * 2
        b = y // 2

    
a, b = map(int,input().split())
num(a, b)
print(a, b)