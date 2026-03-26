food = "Life is too short\nYou need python" # \n 줄 바꾸기
print(food)
print()

#s = set([1, 2, 3])
#s.add(4)
#s.update([5, 6, 7])
#print(s)
print()
numbers = (1,2,3,4,5,6,7,8,9,10) #튜플 언패킹 사용법
(one, *others, ten) = numbers
print(numbers)

fruits = ('apple', 'banana', 'orange', 'grape')
(mine,*yours) = fruits #튜플 언패킹 2
print(yours)
print()
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 4, 5, 6, 7}
set3 = {5, 8, 9, 7, 6, 3}
print(set1)
print(set2)
print(set3)
print(set1.intersection(set2))
print()
my_list = ['오예스', '뭉쉘', '초코파이'] #리스트 활용
my_list[0] = '빅파이'
print(my_list)

my_tuple = ['오예스', '뭉쉘', '초코파이'] #튜플 활용 
print(my_tuple[1])
print()
my_set = {'돈가스', '제육볶음', '보쌈'}
# print(my_set[0])
# my_set[1] = '빅파이'
# my_set.add('닭갈비')
# my_set.remove('돈가스')
# my_set.clear()
# del my_set
# print(my_set)
print()
#a = int(7)
#b = int(3)
#print(a, b)
#print()
#a = 7
#b = 3
#print(a, b)
print()
#a = 5
#b = 3
#print(a, '/', b, '=', a // b, '...', a % b)
#a, b = map(int,input().split())
#a = int(a)
#b = int(b) 
#print(a, '/', b, '=', a // b, '...', a % b)
print()
#a, b, c = map(int,input().split())
#sum = a+b+c
#avg = (a+b+c)//3
#print('sum =', sum)
#print('avg =', avg)
print()
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#e = int(input())
#f = int(input())
#g = int(input())
#print((a + 2), (b - 2), (c * 2), (d / 2), (e // 2), (f % 2), (g ** 2))


#a, b, c, d, e, f, g = map(int,input().split())
#print(a+2, b-2, c*2, d/2, e//2, f%2, g**2)

#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#e = int(input())
#f = int(input())
#g = int(input())
#print(f"{a+2} {b-2} {c*2} {d/2} {e//2} {f%2} {g**2}")
#a = int(input()) #f-string 사용법
#b = int(input())
#print(f'{a} * {b} = {a*b}')

#a = int(input())
#print(a)
#print(a+10)

#a = int(input())#input 활용 f-string 활용
#b = int(input())
#print (f'{a-10} + {b*2} = {a-10+b*2}')

#a = 10
#b = 5
#print(a - b, '=', a, '-', b)
#print(f'{a-b} = {a} - {b}')

#my_set = {'돈가스', '보쌈', '제육덮밥'}
#print(my_set[1])
#my_set[1] = '빅파이'

# a = int(input())
# print(a)
# print(a+10)

#n = int(input())
#print(f"{n}\n{n + 10}") # \n 줄바꿈 표시 
my_list = ['뭉쉘', '초코파이', '빅파이', '빅파이', '빅파이']
print(my_list)
my_set = set(my_list)
print(my_set)
my_list = list(my_set)
print(my_list)