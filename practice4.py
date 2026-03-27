# max = 25 # while활용용
# weight = 0
# item = 3
# while weight + item <= max:
#     weight += item
#     print('짐을 추가합니다')
# print(f'총 무게는{weight}입니다')

# # i =  3
# # while i <= 5:
# #     print(i)
#     i += 1


# drama = ['시즌 1', '시즌 2', '시즌 3', '시즌 4', '시즌 5'] //////////////#break 사용 법
# for x in drama:
#     if x == '시즌 3':
#         print('재미 없대, 그만 보자')
#         break
#     print(f'{x} 시청')

# drama = ['시즌 1', '시즌 2', '시즌 3', '시즌 4', '시즌 5']//////////continue사용법 
# for x in drama:
#     if x == '시즌 3':
#         print('재미 없어, 건너 뛰자')
#         continue
#     print(f'{x} 시청')

#     for x in range(10):
#         if x % 2 == 1:
#             continue
#         print(x)

#         coffee = 10

# products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022'] #//////////////////문자를 찾고 빈 리스트에 추가를 해주는 것것
# recall = []
# for p in products:
#     if p.startswith('SIRO'):
#         recall.append(p)

# print(recall)

# def my_function():
#     print('새로운')
#     print('함수를')
#     print('만들었어요.')

# my_function()
# my_function()

# def show_price(customer):  #함수 정의//////////
#     print(f'{customer} 고객님')
#     print('커트 가격은 1500원 입니다.')

# customer1 = '나장발' # 함수 호출 //////////
# show_price(customer1)

# customer2 = '나수염'
# show_price(customer2)

# def get_price():
#     return 15000

# price = get_price()
# print(f'커트 가격은 {price}원 입니다')     #return ///////////////////////////////


# def get_price(is_vip):
#     if is_vip == True:
#         return 10000
#     else:
#         return 15000

# price = get_price(True)
# print(f'커트 가격은 {price}원 입니다.')            #True False 및 사용
# price = get_price(False)
# print(f'커트 가격은 {price}원 입니다')

# def get_price(is_vip = False):
#     if is_vip == True:
#         return 10000
#     else:
#         return 15000                                    #get_price

# price1 = get_price(True)
# print(price1)
# price2 = get_price()
# print(price2)
# price3 = get_price()
# print(price3)
# price4 = get_price()
# print(price4)


def visit(today,*customers):
    print(today)
    for customer in customers:
        print(customer)

visit('2026년 3월 27일', '나장발')
visit('2026년 3월 27일', '나장발','나수염', '나김리', '강승진')


