import random
A = [3, 5, 2, 1, 4]
for _ in range(4): 
    choicelist = [random.choice(A) for i in range(5)]               #랜덤 사용 법 공부할 것 
    print(choicelist)



print('------------------------------------------------------------------')


A = [3, 5, 2, 1, 4]

lst = [A[3], A[1], A[0], A[2], A[4]]
lst2 = [A[3], A[2], A[1], A[0], A[4]]
lst3 = [A[3], A[2], A[0], A[1], A[4]]
lst4 = [A[3], A[2], A[0], A[4], A[1]]
print(lst)
print(lst2)
print(lst3)
print(lst4)