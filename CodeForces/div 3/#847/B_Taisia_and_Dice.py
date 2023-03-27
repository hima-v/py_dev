from itertools import combinations
from itertools import product
ss=[1,2,3,4,5,6]
for i in range(int(input())):
    n,s,r=map(int,input().split())  #n=4
    maxd=s-r #4th dice stolen
    loc=ss.index(maxd)  #3rd location
    solnspace=[]
    for i in range (1,n): 
        for j in range (1,n):
            solnspace.append(i)
    nd=n-1
    possoln = list(set((combinations(solnspace, nd))))
    vals = [sum(i) for i in possoln]
    for k in range(len(vals)):
        if(vals[k]==r):
                ans=list(possoln[k])           
    ans.append(maxd)
    print(*ans,sep=' ')
    
    #vals= list(map(sum, possoln))
    #ANSWER: [4,x,y,z]  S= 9, R=5 sum of x,y,z=r