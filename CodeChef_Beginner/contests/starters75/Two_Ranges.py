def ran():
    a,b,c,d=map(int,input().split())
    l=[]
    for i in range(a,b+1):
        l.append(i)
    for j in range(c,d+1):
        if(l.count(j)==0):
            l.append(j)
    return(len(l))
for i in range(int(input())):
    print(ran())