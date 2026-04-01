class Soccer:
    def __init__(slef, name, score):
        slef.name = name
        slef.score = score

teams = []

N, M = map(int,input().split())

for i in range(N):
    name, score = input().split()
    score = int(score)
    team = Soccer(name, score)
    teams.append(team)

for team in reversed(teams):
    if team.score >= M:
        print(team.name)




print('-------------------------------------------------------------------')



class SoccerTeam:
    def __init__(self, name, wp):
        self.name = name
        self.wp = wp
    def print_info(self):
        print(self.name, self.wp)

N, M = map(int, input().split())
lst = []
res = []
for i in range(N):
    team_name, wp = input().split()
    lst.append(SoccerTeam(team_name, wp))


for k in range(len(lst)):
    if int(lst[k].wp) >= M:
        res.append(lst[k].name)

for x in range(len(res)-1, -1, -1):
    print(res[x])








    