def scount(n,l1,l2):
    score=0
    streak=[0]
    i=0
    for i in range (0,n):
        if(l1[i]!=0 and l2[i]!=0):
            score+=1
            streak.append(score)
        else:
            score=0
    return(max(streak))
t=int(input())
for i in range (t):
    ndays=int(input())
    chef=list(map(int,input().split()))
    chefina=list(map(int,input().split()))
    print(scount(ndays,chef,chefina))

