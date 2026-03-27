from ntpath import sep


print('C:\\Users\\Nadocoding')
print()
snack = '꿀꽈배기는\n 너무\n 맛있어요'
print(snack)
print()
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic)
print()
name = 'Kim'
age = 15
print(name, 'is', age, 'years old.')
print()
print('{} is {} years old.'.format('Kim', 15))
print()
x = 3
y = 4
print(f'{x} + {y}는 {x + y}입니다.')
print()
num = -50
print(num)
print()

s = set('Hello')
#d = list(s)
#d.sort()
#print(d)
e = list(dict.fromkeys('Hello'))
print(e)
print()
a = [1, 2, 3, 4]
print(a[0])
print()
a = 5
w = 10
print(a, '+', w, '=', (a + w))
print()
print('l''i''k''e', sep ='@')