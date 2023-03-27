for i in range (int(input())):
    n=int(input())
    l=[]
    f=[0]*n
    ini=[]
    for j in range(n):
        a=list(map(int,input().split()))
        l.append(a)
    for k in range(0,n):
        el=l[k][0]
        ini.append(el)
        f[el-1]+=1
    first=(f.index(n-1)+1)
    second=(f.index(1)+1)
    slist=l[ini.index(second)]
    slist.insert(0,first)
    print(*slist,sep=' ')