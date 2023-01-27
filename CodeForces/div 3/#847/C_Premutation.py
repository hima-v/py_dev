for i in range (int(input())):
    n=int(input())
    l=[]
    f=[0]*n
    ini=[]
    for j in range(n-1):
        a=list(map(int,input().split()))
        l.append(a)
    print()
    for k in range(0,n):
        el=l[k][0]
        ini.append(el)
        f[el-1]+=1
    first=(f.index(n)+1)
    second=(f.index(1)+1)
    slist=ini.index(second)
    ans=slist.insert(0,first)
    print(*ans,sep=' ')