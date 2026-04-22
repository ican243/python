class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def like(self):
        print(f'Name:{self.name}, Age:{self.age}')

N = int(input())
people = []

for i in range(N):
    name, age = input().split()
    people.append(person(name, int(age)))

people.sort(key=lambda x: x.age, reverse=True)

for p in people:
    p.like()