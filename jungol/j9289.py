lst = []

while True:
    N = int(input())
    if  N < 1 or N > 5:
        break
    if N % 2 == 0:
        lst.append(N)
a = len(lst)
b = sum(lst)


    
    
print(b // a)


