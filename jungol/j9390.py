a = input()
b = input()
if a == '0':
    a = '00'
if a == '1':
    a = '01'
if a == '2':
    a = '02'
if a == '3':
    a ='03'
if a == '4':
    a ='04'
if a == '5':
    a = '05'
if a == '6':
    a = '06'
if a == '7':
    a = '07'
if a == '8':
    a = '08'
if a == '9':
    a = '09'

if b == '0':
    b = '00'
if b == '1':
    b = '01'
if b == '2':
    b = '02'
if b == '3':
    b = '03'
if b == '4':
    b = '04'
if b == '5':
    b = '05'
if b == '6':
    b = '06'
if b == '7':
    b = '07'
if b == '8':
    b = '08'
if b == '9':
    b = '09'
print(f'{a}:{b}')


#-------------------


time = int(input())
minute = int(input())
print(f'{time:02d}:{minute:02d}')