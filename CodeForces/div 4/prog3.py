def inp():
    t=int(input())
    return t

def mapp():
    p,q=map(int,input().split())
    r,s=map(int,input().split())
    l_in=p+q+s+r
    return l_in

def comparision(leest):
    a=leest[0]
    b=leest[1]
    c=leest[3]
    d=leest[2]
    if(a<b and c<d and a<c and b<d):
        print("Yes")
    else:
        v=v+1
        while(v!=4):
            key=c
            #l_in=a+b+d+c
            l_new=l_in[:3]
            l_new.insert(0, c)
            comparision(l_new)
        if(v==4):
            print("No")
t=inp()
for y in range (t):
    lest=mapp()
    comparision(lest)        

