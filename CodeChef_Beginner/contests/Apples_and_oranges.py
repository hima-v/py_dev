def maxval(n,m):
    k=min(n,m)
    while k!=0:
        if(n%k==0 and m%k==0):
            st=k
            k=0
        else:
            k-=1
    return(st)
t=int(input())
for i in range(t):
    ap,man=map(int,input().split())
    print(maxval(ap,man))