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

letter = 'how are YOU?'
print(letter.lower()) #모두 소문자로 변경
print(letter.upper()) #모두 대문자로 변경
print(letter.capitalize()) #나머지는 다 소문자로 변경 후 첫 글자만 대문자로 변경
print(letter.title()) #영문 단어마다 앞글자 대문자로 변경경
print(letter.swapcase()) #대문자는 소문자로 / 소문자는 대문자로 한 번에 변경 코드
print(letter.split()) #문장을 배열로 만들어주는 코드
str1 = letter.split()
print(str1[0].capitalize())#배열에서 글자 하나를 출력