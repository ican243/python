# num1 = 6   #//try 활용 
# num2 = 0

# try:
#     result = num1 / num2
#     print(num1, num2, '=', end = ' ')
#     print(result)
# except Exception as err:
#     print('에러가 발생했어요', err)
# else:
#     print('정상 동작했어요')
# finally:
#     print('수행종료')


# print('---------------------------------------------') 3//try사용
# num1 = 10
# num2 = 0

# try:
#     reslut = num1 / num2
#     print(f'연산 결과는 {reslut}입니다.')
# except Exception as err:
#     print('에러가 발생했어요 : ', err)
# except ZeroDivisionError:
#     print('0으로 나눌 수 없어요')
# except TypeError:
#     print('값의 형태가 이상해요')

# import goodjob                              #//import, from을 사용한 코드
# goodjob.say()

# from goodjob import say
# say()

# import random
# # my_list = ['가위', '바위', '보']     #random 사용 
# # print(random.choice(my_list))
# print(random.random())   



#------------------------------------------------------------

# import nadocoding.goodjob

# nadocoding.goodjob.say()


# from nadocoding import goodbye
# goodbye.bye()

from nadocoding import goodjob, goodbye
goodjob.say()
goodbye.bye()