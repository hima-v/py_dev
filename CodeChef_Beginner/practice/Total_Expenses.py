def price(q,pp):
    cp=q*pp
    if(q>1000):
        cp=cp-0.1*cp
    return(float(cp))
t=int(input())
for i in range (t):
    q,pp=map(int,input().split())
    print(price(q,pp))
