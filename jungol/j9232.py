x = float(input())

if x <= 50.80:
    print('Flyweight')
elif x <= 61.23:
    print('Lightweight')
elif x <= 72.57:
    print('Middleweight')
elif x <= 88.45:
    print('Cruiserweight')
else:
    print('Heavyweight')