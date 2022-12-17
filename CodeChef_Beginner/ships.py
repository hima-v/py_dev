sc=["BattleShip","Cruiser","Destroyer","Frigate"]
id=[]
t=int(input())
for i in range(t):
    el=(input())
    id.append(el)
print(id)
for idval in id:
    print(idval)
    if(idval.upper()=='B'):
        print(sc[0])
    if(idval.upper()=='C'):
        print(sc[1])
    if(idval.upper()=='D'):
        print(sc[2])
    if(idval.upper()=='F'):
        print(sc[3])