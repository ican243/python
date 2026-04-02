# class baseball:
#     def __init__(self, name, tasu, ang):
#         self.name = name
#         self.tasu = tasu
#         self.ang = ang

#     def like(self):
#         print(f'name:{self.name}, AVG:{self.ang/self.tasu:.3f}, AB:{self.tasu}, H:{self.ang}')
        
# name1, tasu1, ang1 = input().split()
# name2, tasu2, ang2 = input().split()

# b1 = baseball(name1, int(tasu1), int(ang1))
# b2 = baseball(name2, int(tasu2), int(ang2))

# b1.like()
# b2.like()

class baseball:
    def __init__(self, name, tasu, ang):
        self.name = name
        self.tasu = tasu
        self.ang = ang
    def like(self):
        print(f'name:{self.name}, AVG:{self.ang / self.tasu:.3f}, AB:{self.tasu}, H:{self.ang}')

name, tasu, ang = input().split()
name2, tasu2, ang2 = input().split()


b1 = baseball(name, int(tasu), int(ang))
b2 = baseball(name2, int(tasu2), int(ang2))

b1.like()
b2.like()





























