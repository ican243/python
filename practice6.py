# f = open('list.txt', 'w', encoding = 'utf-8') ##// open encoding활용용
# f.write('임진휘\n')
# f.write('장서연\n')
# f.write('성현태\n')
# f.write('김선재\n')
# f.close()

# f = open('list.txt', 'r', encoding = 'utf-8')
# for line in f:
#     print(line, end = '')
# f.close()



# class BlackBox: // class활용 
#     pass

# b1 = BlackBox()
# b1.name = '까망이'
# print(b1.name)
# print(isinstance(b1, BlackBox))

# class BlackBox:
#     def __init__(self, name, price):   #//////////__init__ 활용
#         self.name = name
#         self.price = price

# b1 = BlackBox('까망이', 200000)
# print(b1.name, b1.price)
# b2 = BlackBox('하양이', 100000)
# print(b2.name, b2.price)


# class BlackBox:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def set_travel_mode(self,min):
#         print(str(min)+ '분 동안 여행 모드 ON')

# b1 = BlackBox('까망이', 200000)
# b1.set_travel_mode(30)





class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def show(self):
        print(f'{self.name} {self.age} {self.job}')

p = Person(name="진휘", age=28, job="개발자")
p.show()



class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def show(self):
        print(f'{self.name} {self.age} {self.job}')


# 입력 받기
name = input("이름: ")
age = int(input("나이: "))
job = input("직업: ")

p = Person(name, age, job)
p.show()