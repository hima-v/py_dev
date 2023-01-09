n,m,k=map(int,input().split())
c=0
for i in range(n):
    l=list(map(int, input().split()))
    if(l[k]<=10):
        p=sum(l,-l[k])
        if(p>=m):
            c+=1
print(c)