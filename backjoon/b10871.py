# a, b = map(int,input().split())
# M = list(map(int,input().split()))    #//for 사용용
# # print(a, b)
# # print(M)
# for num in M:
#     if num < b:
#         print(num, end=' ')

# a, b = map(int,input().split())
# M = list(map(int,input().split())) #while 사용용

# i = 0
# while i < len(M):
#     if M[i] < b:
#         print(M[i], end = ' ')
#     i += 1

# i = 1
# while i <= 5:
#     print(i)
#     i += 1





#///// 연습문제  
target = 'dlawlsgnl'

while count < 5:
    guess = input('비밀번호를 입력하세요: ')
    count += 1

    if guess == target:
        print('환영합니다!') 
        break
    else:
        print(f'비밀번호를 다시 입력하세요. (남은 기회{5 - count}번)')
    if count == 5 and guess != target:
        print('입력 횟수를 초과했습니다. 계정이 잠깁니다.')
     