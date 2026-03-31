# def line(a, b):
#     print(f'{a} 곱하기 {b} = {a * b}') ////////////함수 활용용

# line(1, 2)
# line(1, 3)
# line(4, 6)

# def func(a, b):
#     return a * b

# c = func(3, 9)
# print(c)

# def secret():
#     message = '이건 나만의 비밀'   #secret 힘수 활용
#     print(message)
# message = '함수 내에서는 자우롭게 수정이 가능해요'
# def please():
#     message = '이렇게 하면 되지?'                ////////////지역 변수 
#     print(message)

# message2 = '이것도 비밀'
# print(message2)
# secret()
# please()

message = '나는야 전역 변수'
print(message)

def no_secret():
    global message
    message = '이러면 또 지역 변수'             #//////////////// 전역 변수 
    print(message)
no_secret()
print(message)


