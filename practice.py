print('hello world') #자기소개 
print('나는 임진휘')
print("공부를 시작했다")
print('----------연산자------------') #연산자 활용
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5%2)
print('------------비교 연산자---------') #비교 연산자 활용 
print(5>2)
print(5>=2)
print(5<2)
print(5<=2)
print(5 == 2)
print(5 != 2)

print()

print(3<5 and 7<5)
print(3<5 or 7<5)
print(not 3<5)

print()

print('c' in 'cat')
print('c' not in 'cat')
print('--------------sep, enumerate 활용 -------------')
x, y = 5, 7
print(x, y, sep = "*")
print("Hello", "JinHwi", sep = "")

seasons = ['spring', 'summer', 'fall', 'winter']
list(enumerate(seasons))
for idx, val in enumerate(seasons):
    print(idx, val)
print()
'''
name = '임진휘'
print(name)
print()
name = input("이름입력: ")
print(name)
print()
age = int(input("나이입력: "))
print = (age + 1)
'''
