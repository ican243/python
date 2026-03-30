# a, b, c = input().split()
# print(f'location: {a}')
# print(f'bedrooms: {b}')
# print(f'bathrooms: {c}')

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        print(f'My name is {self.name}.')
        print(f'I am {self.age} years old.')

name, age = input().split()
#print(name, age)
p1 = person (name, age)
p1.print()


# class hotel:
#     def __init__(self, name, bed, bath):
#         self.name = name
#         self.bed = bed
#         self.bath = bath

# h1 = input()