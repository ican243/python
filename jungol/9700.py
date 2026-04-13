class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def __add__(self, other):
        return Person(self.height + other.height, self.weight + other.weight)
    def __sub__(self, other):
        return Person(abs(self.height - other.height), abs(self.weight - other.weight))
    def __truediv__(self, num):
        return Person(self.height / num, self.weight / num)
    def __floordiv__(self, num):
        return Person(self.height // num, self.weight / num)
    def __str__(self):
        return f"키: {self.height}, 몸무게: {self.weight:.1f}"


h1, w1 = input("당신의 키와 몸무게를 입력하세요.").split()
h2, w2 = input("친구의 키와 몸무게를 입력하세요.").split()

p1 = Person(int(h1), float(w1))   
p2 = Person(int(h2), float(w2))

print("my", p1)
print("friend", p2)
print("plus", p1 + p2)
print("minus", p1 - p2)
print("avg", (p1 + p2) // 2)




class person:
    def __init__(self, A, B):
        self.A = int(A)
        self.B = float(B)

A1, B1 = input('당신의 키와 몸무게를 입력하세요.').split()

A2, B2 = input('친구의 키와 몸무게를 입력하세요.').split()

me = person(A1, B1)
friend = person(A2, B2)


print(f'my 키: {me.A}, 몸무게: {me.B}')
print(f'friend 키: {friend.A}, 몸무게: {friend.B}')
print(f'plus 키: {me.A+friend.A} 몸무게: {me.B+friend.B}')
print(f'minus 키: {me.A-friend.A} 몸무게 {abs(me.B-friend.B):.1f}')
print(f'avg 키: {(me.A+friend.A)//2} 몸무게 {(me.B+friend.B)/2:.1f}')