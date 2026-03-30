x = int(input()) #//def ㅎ마수 사용 방법

def plus(x):
    print(f'{x} + 10 = {x + 10}')
def minus(x):
    print(f'{x} - 10 = {x - 10}')

plus(x)
minus(x)



print('----------------------')

x = int(input())   #//return 사용 방법법
def plus(x):
    return x + 10

def minus(x):
    return x - 10

print(f'{x} + 10 = {plus(x)}')
print(f'{x} - 10 = {minus(x)}')
