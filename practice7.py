class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_travel_mode(self, min):
        print(f'{self.name} {min}분 동안 여행 모드 ON') #//메소드를 정희할 때 처음 전달값은 반드시 self, self.name과 같은 형태로 멤버변수를 사용

b1 = BlackBox('까망이', 200000)
b2 = BlackBox('하양이', 100000)

b1.set_travel_mode(20)
b2.set_travel_mode(10)
BlackBox.set_travel_mode(b1, 25)