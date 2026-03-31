class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def student(self):
        if self.age >= 18:
            print(f'{self.name}({self.age}) : adult')
        else:    
            print(f'{self.name}({self.age}) : child')

name1, age1 = input().split()
name2, age2 = input().split()
s1 = person(name1, int(age1))
s2 = person(name2, int(age2))

s1.student()
s2.student()


class baseball:
    def __init__(self, name, tasu, ang):
        self.name = name
        self.tasu = tasu
        self.ang = ang

    def like(self):
        print(f'name:{name}, AVG:{ang/tasu}, AB{tasu}, H:{ang}')
name1, tasu1, ang1 = input().split()
name2, tasu2, ang2 = input().split()

b1 = baseball(name1, int(tasu1), int(ang1))
b2 = baseball(name2, int(tasu2), int(ang2))

b1.like
b2.like
