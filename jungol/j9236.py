a, b = input().split()
b = int(b)

if a == "M":
    if b >= 19:
        print('MAN')
    else:
        print('BOY')
else:
    if b >= 19:
        print('WOMAN')
    else:
        print('GIRL')
    
