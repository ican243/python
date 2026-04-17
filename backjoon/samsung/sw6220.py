# a = int(input())
# b = input()
# for i in range(a):
#     for j in range(a):
#         print()

a = int(input())
for i in range(1, a+1):
    b = input()
    if 'a'== b or 'b'== b or 'c'== b or 'd'== b or 'e'== b or 'f'== b or 'g'== b or 'h'== b or 'i'== b or 'j'== b or 'k'== b or 'l'== b or 'm'== b or 'n'== b or 'o'== b or 'p'== b or 'q'== b or 'r'== b or 'x'== b or'y'== b or 'z'== b: 
        print(f'#{i} {b} 는 소문자 입니다.')
    else:
        print(f'#{i} {b} 는 대문자 입니다.')