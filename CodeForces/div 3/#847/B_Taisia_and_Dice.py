from itertools import combinations
from itertools import product
ss=[1,2,3,4,5,6]
for i in range(int(input())):
    n,s,r=map(int,input().split())
    maxd=s-r
    loc=ss.index(maxd)
    if(loc==0):
        solnspace=[1]
    else:
        solnspace=ss[:loc]
    nd=n-1
    possoln=[p for p in product(solnspace, repeat=n)]
    vals= list(map(sum, possoln))
    for k in range(len(vals)):
        if(vals[k]==r):
            if(len(possoln[k] == n-1)):
                ans=list(possoln[k])           
    ans.append(maxd)
    print(*ans,sep=' ')