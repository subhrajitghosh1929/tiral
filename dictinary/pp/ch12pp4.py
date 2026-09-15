d = {}
ans = "y"
while ans == "y" or ans == "Y" :
    name = input("Enter Team name: ")
    w = int(input("Enter number of wins: "))
    l = int(input("Enter number of losses: "))
    d[name] = [w, l]
    ans = input("Do you want to enter more team names? (y/n): ")
team = input("Enter team name for winning percentage: ")
if team not in d:
    print("Team not found", team)
else:
    wp = d[team][0] / sum(d[team]) * 100
    print("Winning percentage of", team, "is", wp)
w_team = []   
for i in d.values():
    w_team.append(i[0]) 
print("Number of wins of each team", w_team)
w_rec = []
for i in d:
    if d[i][0] > 0:
        w_rec.append(i)
print("Teams having winning records are:", w_rec)
