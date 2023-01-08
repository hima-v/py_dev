def route(x,y,z):
    if((x+y)>z):
        s="TRAIN"
    if((x+y)<z):
        s="PLANEBUS"
    if(x+y==z):
        s="EQUAL"
    return(s)
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print(route(x,y,z))
    