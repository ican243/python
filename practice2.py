lang = 'python'
print(lang)
print(lang[0])
print(lang[-1])
print(lang[:3])
print(lang[2:])
print(lang[:])
print(lang[:-1])


num = 3
num += 2 #num = num + 2
print(num)

num -= 1
num *=2
num /=4
print(num)

print()

snack = '꿀꽈배기'
print(len(snack)) #snack 글자가 몇 글자인지 확인하기기
snack = '''꿀꽈배기는
너무
맛있어요'''
print(snack)

print()

print('-' * 10) #문자 곱하기를 하여 나오게 하기기
print('NadoCoding')
print('*' * 10)

print()

letter = 'how are you?'
print(letter.lower()) #모두 소문자로 변경 
print(letter.upper()) #모두 대문자로 변경
print(letter.capitalize()) #나머지는 다 소문자로 변경 후 첫 글자만 대문자로 변경
print(letter.title()) #영문 단어마다 앞글자 대문자로 변경경
print(letter.swapcase()) #대문자는 소문자로 / 소문자는 대문자로 한 번에 변경 코드
print(letter.split()) #문장을 배열로 만들어주는 코드
str1 = letter.split()
print(str1[0].capitalize()) #배열에서 글자 하나를 출력
print(letter.count('how')) #문장에 단어가 몇 개가 들어가있는지 확인할 수 있는 코드 / 특정 단어의 수
print(letter.count('o'))
print()

s = '나도고등학교'
print(s.startswith('나도')) #시작하는 문자열이 똑같은지지 / true&false
print(s.endswith('초등학교')) #끝나는 문자열이 똑같은지 / true&false
s2 = '...나도고등학교...'
print(s2.strip('.'))
s3 = '.,.나도고등학교.,.' #strip에 대해서 검색 필요
print(s3.strip('.'))
print(s.replace('고등학교', '고교'))
s4 = '나도고교너도고교'
print(s4.replace('고교', '고등학교')) #글자를 바꿔주는 코드
print(s.find('학교')) #글자 첫 번째 위치를 인덱스(번호로) 알려주는 코드
print(s.find('너도')) # 해당값이 존재하지 않을 떄 -1 음수로 표현
print(s.center(10,'-')) #부분에 문자를 넣는 메소드드

letter = 'pulljima'
print(len(letter))  

