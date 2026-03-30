a, b = map(int,input().split())

def plus():
    return(a+b)
def minus():
    return(abs(a-b))

print(f'두 수의 합 = {plus()}')
print(f'두 수의 차 = {minus()}')   #abs 활용 및 return 활용