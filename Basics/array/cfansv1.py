print(*ans,sep='')
possoln = list(combinations(ss,nd))
d=[]
d1=s-r
le=0
ri=ss.index(d1)
solnspace=ss[:ri]
mid=ri//2
for j in range(n-1):
if(sum(solnspace)==r):
    print(solnspace)
elif(sum(solnspace)>r):
    solnspace=solnspace[:]