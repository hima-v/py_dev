def gmine(l):
    if((l[0]+1)*l[2]>=l[1]):
        return("YES")
    else:
        return("NO")
t=int(input())
x=[]
for i in range (t):
    li=list(map(int,input().split()))
    x.append(gmine(li))
for val in x:
    print(val)